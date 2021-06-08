from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = get_sources('business')
	sports_news = get_sources('sports')
	technology_news = get_sources('technology')
	entertainment_news = get_sources('entertainment')
	title = "News Central"

	return render_template('index.html',title = title, sources = sources,sports_news = sports_news,technology_news = technology_news,entertainment_news = entertainment_news)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles) 