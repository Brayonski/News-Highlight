import urllib.request, json
from .models import source

Sources = source.Sources
Articles = source.Articles

# Getting api key
api_key = None
base_url = None
articles = None
def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    articles_url = app.config['ARTICLES_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        sources_results = None

        if get_news_response['sources']:
            sources_results_list = get_news_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

# processing results
def process_results(source_list):
    '''
    Function that processes the sources result and transform them to a list of objects
    Args:
        source_list: A list of dictionaries that contain sources details
    Return:
        sources_results: A list of sources objects
    '''
    sources_results = []
    for source_item in source_list:
        id = source_item.get('id')
        title = source_item.get('name')
        overview = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        if url:
            news_object = Sources(
                id, title, overview, url, category, country)
            sources_results.append(news_object)
    return sources_results


def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(source, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        print(get_articles_response)
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = obtain_results(articles_results_list)

    return articles_results

#obtaining articles results

def obtain_results(articles_list):
    '''
    Function that processes the articles results and transform them to a list of objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Return:
        articles_results: A list on articles objects
    '''
    

    articles_results = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        url = article_item.get('url')

        article_object = Articles(id,author,title,description,url,urlToImage,publishedAt, url)
        articles_results.append(article_object)
        return articles_results


