from flask import render_template
from app import app
from request import get_sources,get_articles
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

# @app.route('/')
# def articles():
#     '''
#     View root page function that returns the articles page and its data
#     '''
#     #Getting articles news feed
#     news_articles = get_articles('myarticles')
#     print(news_articles)
#     title = 'Articles'
#     return render_template('articles.html', title = title, myartcles = news_articles)

# @app.route('/articles/<int:articles_id>')
# def articles(articles_id):
#     '''
#     View articles page function that returns the articles page and its data
#     '''
#     return render_template('articles.html', id = articles_id)

