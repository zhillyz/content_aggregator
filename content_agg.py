from abc import ABC, abstractmethod
from dotenv import load_dotenv
from newsapi import NewsApiClient
from email_content import sendEmail
import io
import praw
import os
import requests
import json
import matplotlib.pyplot as plt
import datetime

load_dotenv()
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

    def __init__(self,query,subreddit='all',limit=10) -> None:
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
    def __init__(self,station,live=False):
        self.url = f'https://api.tfl.gov.uk/crowding/{station}/'
        days=['MON','TUE','WED','THU','FRI','SAT','SUN']
        self.dateObj = datetime.datetime.now()
        self.station = station
        day=self.dateObj.weekday()
        if live:
            self.url = self.url + "Live"
        else:
            self.url = self.url + str(days[day])

    def connect(self):
        pass
    
    def fetch(self):
        self.buf = io.BytesIO()
        self.crowding = requests.get(url=self.url)
        crowding_dict = json.loads(self.crowding.content.decode('utf-8'))
        time_bands = crowding_dict['timeBands']
        x=[]
        y=[]
        for band in time_bands:
            x.append(band['timeBand'])
            y.append(band['percentageOfBaseLine'])
        fig, ax = plt.subplots()
        fig.canvas.draw()
        ax.plot(x,y)
        leftAm = [tick for tick in x if crowding_dict['amPeakTimeBand'].split('-')[0] in tick][0]
        rightAm = [tick for tick in x if crowding_dict['amPeakTimeBand'].split('-')[1] in tick][0]
        leftPm = [tick for tick in x if crowding_dict['pmPeakTimeBand'].split('-')[0] in tick][0]
        rightPm = [tick for tick in x if crowding_dict['pmPeakTimeBand'].split('-')[1] in tick][0]
        plt.axvspan(leftAm,rightAm, color = 'red', alpha = 0.5, label = 'Peak Times')
        plt.axvspan(leftPm,rightPm, color = 'red', alpha = 0.5)
        minsRound = 15*(round(float(self.dateObj.minute)/15))
        minsRound = minsRound if minsRound != 60 else 0
        now = self.dateObj.replace(minute=minsRound).strftime('%H:%M')
        nowX = [pos for pos in x if now in pos][0]
        plt.axvline(nowX,color='g', label = 'Time just now')
        loc = plt.MaxNLocator(10) # this locator puts ticks at regular intervals
        ax.xaxis.set_major_locator(loc)
        labels = [item.get_text()[6:] for item in ax.get_xticklabels()]
        ax.set_xticklabels(labels)
        ax.legend()
        ax.set_xlabel('Time')
        ax.set_ylabel('% of Baseline')
        plt.savefig('graph.png')
        self.fig = 'graph.png'

    def email(self):
        sendEmail(f'Peak busy times for: {self.station}',self.fig,attach=True)

if __name__ == '__main__':
    # reddit_top_programming = RedditHotTopics('ukraine',subreddit='news',limit=10)
    # print(reddit_top_programming)
    # news = NewsSource('ukraine')
    # print(news)
    crowding = TFLCrowding('940GZZLUCHX')
    crowding.fetch()
    crowding.email()