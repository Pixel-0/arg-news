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


@main..route('/search/,article_name>')
def articles(source_id):
    '''
    renders the artices template
    '''

    #getting articles
    article = get_articles(source_id)
    title = f'{ source_id }'

    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name = search_article))
    else:
        return render_template('article.html',title = title, articles = article)
        
    