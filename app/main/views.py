from flask import render_template,request
from . import main
from ..request import get_sources,get_articles
# Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular News feed
    enter= get_sources('general')
    
    title = 'Home - Welcome to The best News  Website Online'
    return render_template('index.html', title = title, enter = enter)

@main.route('/articles/<id>')
def articles(id):
    '''
    Articles
    '''
    news = get_articles(id)
   
    title = 'Articles'
    return render_template('articles.html', title = title, news = news)



