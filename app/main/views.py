from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_newsource,get_articles,search_article
from ..models import Source,Article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    general_newsource = get_newsource('general')
    technology_newsource = get_newsource('technology')
    entertainment_newsource = get_newsource('entertainment')
    sports_newsource = get_newsource('sports')
    business_newsource = get_newsource('business')
    science_newsource = get_newsource('science')

    return render_template('index.html',general = general_newsource, technology = technology_newsource, entertainment = entertainment_newsource, sports = sports_newsource, business= business_newsource, science = science_newsource)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    View article page function returns the articles based on a new source
    '''

    #Getting articles
    article = get_articles(source_id)
    title = f'{source_id}'
    
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('article.html', title=title,articles=article)

@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
      
    return render_template('search.html',title = title,articles=searched_articles)