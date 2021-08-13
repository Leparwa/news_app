from flask import render_template
from app import app
from ..request import get_news
 

# @app.route('/')
# def index():

#     '''
#     View root page function that returns the home page and its data
#     '''
#       # Getting News sources
#     news_sources = get_news('sources')
#     return render_template('home_page.html' , sources = news_sources)
