from app import app
import urllib.request, json
from models import news

Sources = news.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the sources base url
base_url = app.config["SOURCES_API_BASE_URL"]
#getting the articles base url
articles_url = app.config["ARTICLES_API_BASE_URL"]



def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def get_articles(articles):
    '''
    Function that gets the json response to url request
    '''
    get_source_url = base_url.format(articles, api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['articles']:
            source_results_list = get_source_response['articles']
            source_results = obtain_results(source_results_list)
    
    return source_results

# processing results


def process_results(news_list):
    '''
    Function that processes the news result and transform them to a list of objects
    Args:
        news_list: A list of dictionaries that contain news details
    Return:
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('name')
        overview = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
        if url:
            news_object = Sources(
                id, title, overview, url, category, country)
            news_results.append(news_object)
    return


    

def 


