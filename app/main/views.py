from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news
from ..models import Review

# Views
@main.route('/')
def index():
   news_sources = get_news('sources')
   return render_template('home_page.html', sources=news_sources)