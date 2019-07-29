import urllib.request,json
from .models import Source
from .models import Article

# Getting api key
api_key = None
# Getting the Category url
sources_url = None
#Getting the Article url
everything_url = None
#Search url
search_url = None



def configure_request(app):
    global api_key,everything_url,search_url,sources_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    everything_url=app.config['EVERYTHING_BASE_URL']
    search_url=app.config["SEARCH_API_BASE_URL"]

def get_newsource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsource_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_newsource_url) as url:
        get_newsource_data = url.read()
        get_newsource_response = json.loads(get_newsource_data)


        newsource_results = None

        if get_newsource_response['sources']:
            newsource_results_list = get_newsource_response['sources']
            newsource_results = process_results(newsource_results_list)

    return newsource_results


def process_results(newsource_list):
    '''
    Function  that processes the new source result and transform them to a list of Objects
    Args:
        newsource_list: A list of dictionaries that contain news source details
    Returns :
        newsource_results: A list of newsource objects
    '''
    newsource_results = []
    for news_item in newsource_list:
        id = news_item.get('id')
        name = news_item.get('title')
        title = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        newsource_object = Source(id,title,name,description,url)
        newsource_results.append(newsource_object)

    return newsource_results

def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = everything_url.format(source_id,api_key)
 

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the new articles and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details
    Returns :
        articles_results: A list of article objects
    '''
    articles_results = []
    for article_item in articles_list:
     
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        

        if urlToImage:
            articles_object = Article(title, description, url, urlToImage)
            articles_results.append(articles_object)

    return articles_results

def search_article(article_name):
    get_search_url = search_url.format(article_name,api_key)

    with urllib.request.urlopen(get_search_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)
        print (search_article_response)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_articles(search_article_list)

    return search_article_results
