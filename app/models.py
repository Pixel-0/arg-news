class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,title,description,url):
        self.id =id
        self.name=name
        self.title = title
        self.description = description
        self.url = url
        



class Article:

    '''
    Aticle class to define Article Objects
    '''


    def __init__(self,title,description,url,urlToImage):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
