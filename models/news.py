class Sources:
    def __init__(self,id,title,overview,url,category,country):
        self.id =id
        self.title = title
        self.overview = overview
        self.url = url
        self.category = category
        self.country = country

class Articles:
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = descrition
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
