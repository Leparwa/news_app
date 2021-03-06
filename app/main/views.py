from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news, get_source_news
from ..models import Review

# Views
@main.route('/')
def index():
   news_sources = get_news('/sources?')
   return render_template('home_page.html', sources=news_sources)

@main.route('/source/<string:id>')
def get_source(id):
   endpoint = '?sources'+'='+id+'&'
   news_source = get_source_news(endpoint)
   return render_template('news_source.html', source=news_source)