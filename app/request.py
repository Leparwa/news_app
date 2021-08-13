import urllib.request,json
from .models import News, news_article

# Getting api key
apiKey = None
# Getting the news base url
base_url = None

def configure_request(app):
    global apiKey,base_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(endpoint):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(endpoint, apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)


        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def get_source_news(endpoint):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(endpoint, apiKey)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_articles = url.read()
        get_articles_response = json.loads(get_source_articles)

        if get_articles_response['articles']:
            articles_results = get_articles_response['articles']
            # articles_results_list = get_articles_response['articles']
            # articles_results = process_results(articles_results_list)


    return articles_results

    
def process_articles_results(articles_results_list):
    '''
    Function  that processes the News result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    articles_results = []
    for article_item in articles_results_list:
        source = article_item .get('source')
        author = article_item .get('author')
        title = article_item .get('title')
        url = article_item .get('url')
        description = article_item .get('description')
        urlToImage = article_item .get('urlToImage')
        publishedAt = article_item .get('publishedAt')
        content = article_item .get('content')
        articles_object = news_article(source,description,url, title, urlToImage, publishedAt, content, author)
        articles_results.append(articles_object)

    return articles_results 

def process_results(news_list):
    '''
    Function  that processes the News result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
        language = news_item.get('language')


        news_object = News(id,name,description,url,category,country, language)

        news_results.append(news_object)

    return news_results