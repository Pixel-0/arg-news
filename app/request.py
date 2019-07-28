import urllib.request, json
from .models import Source
from .models import Article

#Getting api key
api_key = None

#getting categorey url
sources_url = None

#Getting the article url
article_url = None

#search_url
search_url=None

def configure_request(app):
    global api_key, article_url,search_url,sources_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    article_url = app.config[' ARTICLES_BASE_URL']
    search_url = app.config['SEARCH_BASE_URL']

def get_news_Sources(category):
    '''
    Gets json response
    '''
    get_news_Sources_url = sources_url.format(category, api_key)

    with urllib.request.urlopen(get_news_Sources_url) as url:
        get_news_Sources_data = url.read()
        get_news_Sources_response = json.loads(get_news_Sources_data)

        news_sources_result = None

        if get_news_Sources_response['sources']:
            news_sources_results_list = get_news_Sources_response['sources']
            news_sources_result = process_results(news_sources_results_list)

    return news_sources_result

def process_results(news_sources_results_list):
    '''
    function to process json data into class objects
    '''
    news_sources_result = []

    for news_item in news_sources_result:
        id = news_item.get('id')
        name = news_item.get('title')
        title = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get(url)


        news_sources_object = Source(id, title,name,description,url)
        news_sources_result.append(news_sources_object)
        
    return news_sources_result

def get_articles(Source_id):
    '''
    function to get article json results 
    '''
    get_articles_url = article_url.format(Source_id.api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results
