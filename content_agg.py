from abc import ABC, abstractmethod
from newsapi import NewsApiClient
import logging
import praw
import os
import requests

CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')
NEWS_API = os.environ.get('NEWS_API')

class Source(ABC):
    ''' base source class which will be inherited by different source child
    classes such as Reddit etc. Architecture will be Source > Specific source > sub topic of that source'''
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def fetch(self):
        pass

class RedditSource(Source):
    '''Reddit source'''
    def connect(self):
        self.reddit_con = praw.Reddit(client_id = CLIENT_ID,
                                      client_secret=CLIENT_SECRET,
                                      grant_type_access='client_credentials',
                                      user_agent='script/1.0')
        return self.reddit_con
    
    def fetch(self):
        pass

class RedditHotTopics(RedditSource):

    def __init__(self,query,subreddit='news',limit=10) -> None:
        self.reddit_con = super().connect()
        self.hot_submissions = []
        self.subreddit = subreddit
        self.query = query
        self.limit = limit
        self.fetch()
        
    def fetch(self):
        self.hot_submissions = self.reddit_con.subreddit(self.subreddit).search(query=str(self.query),limit=self.limit,sort='hot')

    def __repr__(self):
        urls = []
        for submission in self.hot_submissions:
            urls.append(vars(submission)['url'])
        return '\n'.join(urls)
    
class NewsSource(Source):
    ''' using news api modules
    Sources can be chosen from https://newsapi.org/docs/endpoints/sources'''

    def __init__(self,query):
        self.query = query
        self.connect()
        self.fetch()

    def connect(self):
        self.news_con = NewsApiClient(api_key = NEWS_API)

    def fetch(self):
        self.articles = self.news_con.get_top_headlines(q=self.query)
    
    def __repr__(self):
        articles = []
        if self.articles['articles']:
            for article in self.articles['articles']:
                articles.append('Title: %s}'%article['title'])
                articles.append('URL: %s'%article['url'])
        return '\n'.join(articles)

class TFLCrowding(Source):
    ''' simple http request api to transport for london'''
    def __init__(self,station,day=None,live=False):
        self.url = f'https://api.tfl.gov.uk/crowding/{station}/'
        if day:
            if live:
                live = False
                logging.warning("Can\'t have day query and Live so setting Live to False")
            self.url = self.url + str(day)
        if live:
            self.url = self.url + "Live"

    def connect(self):
        pass
    
    def fetch(self):
        self.crowding = requests.get(url=self.url)
        print('test')

if __name__ == '__main__':
    # reddit_top_programming = RedditHotTopics('ukraine',subreddit='news',limit=10)
    # print(reddit_top_programming)
    # news = NewsSource('ukraine')
    # print(news)
    crowding = TFLCrowding('940GZZLUCHX')
    crowding.fetch()