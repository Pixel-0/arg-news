from flask import render_template, request,redirect,url_for
from . import main
from ..request import  get_news_Sources,get_articles

@main.route('/')
def index():
    '''
    view root page function that returns the index page
    '''
     
     #getting news sources
    general_newssource = get_news_Sources('general')
    technology_newssource = get_news_Sources('technology')
    entertainment_newssources = get_news_Sources('entertainment')
    sports_newssources = get_news_Sources('sports')
    business_newssource = get_news_Sources('business')
    science_newssource = get_news_Sources('science')

    return render_template('index.html', general = general_newssource, technology = technology_newssource, entertainment = entertainment_newssources, sports = sports_newssources, business = business_newssource, science = science_newssource)


@main.route('/article/<source_id>')
def articles(Source_id):
    '''
    renders the artices template
    '''

    #getting articles
    article = get_articles(Source_id)
    title = f'{ Source_id }'

    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name = search_article))
    else:
        return render_template('article.html',title = title, articles = article)


# @main.route('/search/<article_name>')
# def search(article_name):
#     '''
#     displays search results
#     '''
#     article_name_list = article_name.split(" ")
#     article_name_format = "+".join(article_name_list)
#     searched_articles = search_article(article_name_format)