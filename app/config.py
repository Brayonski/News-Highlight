class Config:
    '''
    General configuration parent class
    '''

    SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?category{}&apiKey={}'
    ARTICLES_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True