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