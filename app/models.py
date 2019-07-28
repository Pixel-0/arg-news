class Source:
    '''
    Source class for news source objects
    '''
    def __init__(self,id,name,title,description, url):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url

class Article:
    '''
    Class to define article Objects
    '''
    def __init__(self,id,title,description, url, urlToImage):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage

