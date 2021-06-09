import urllib.request
import json
from .models import News,Articles
from datetime import datetime

#getting the api key
api_key = None

#getting the news base_url
base_url = None

#getting the articles_url
articles_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['ALL_NEWS_API_URL']
    articles_url = app.config ['ARTICLES_BASE_URL']




def get_news(category):
    '''
    Functions that gets the json response to our url request
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



def process_results(news_list):
    '''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
    '''

    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        author = news_item.get('author')
        url = news_item.get('url')
        country = news_item.get('country')
        description = news_item.get('description')
        category = news_item.get('category')
        id = news_item.get('id')

        
        news_object = News(name, author,url , description,country, category,id)
        news_results.append(news_object)

    return news_results



def get_articles(source_id):
    '''
	Function that processes the articles and returns a list of articles objects
    '''

    get_article_url = articles_url.format(source_id, api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results




def process_articles(articles_list):
    '''
	     Function  that processes the news result and transform them to a list of Objects

    '''
    articles_results = []
    for article_item in articles_list:
        title = article_item.get('title')
        description = article_item.get('description')
        image = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        author = article_item.get('author')
        url = article_item.get('url')


        if image:
            article_object = Articles(title, description, image, publishedAt, author, url)
            articles_results.append(article_object)
            
    return articles_results


