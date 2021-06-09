class News:
    '''
    Sources class to define sources objects
    '''

    def __init__(self, name, author, url,description, country,category, id):
        self.name = name
        self.author = author
        self.url = url
        self.description = description
        self.country = country
        self.category = category
        self.id = id

class Articles:
    '''
    Articles class to define objects
    '''

    def __init__(self, title, description, image, publishedAt, author, url):
        self.title = title
        self.description = description
        self.image = image
        self.publishedAt = publishedAt
        self.author = author
        self.url = url