from flask import render_template
from app import app
from request import get_sources
# Views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular News feed
    popular_news= get_sources('popular')
    print(popular_news)
    title = 'Home - Welcome to The best News  Website Online'
    return render_template('index.html', title = title, popular = popular_news)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html', id=news_id)
