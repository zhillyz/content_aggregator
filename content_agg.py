from abc import ABC, abstractmethod
import praw
import os

CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')

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

    def __init__(self,subreddit) -> None:
        self.reddit_con = super().connect()
        self.hot_submissions = []
        self.subreddit = subreddit
        
    def fetch(self, limit: int):
        self.hot_submissions = self.reddit_con.subreddit(self.subreddit).hot(limit=limit)

    def __repr__(self):
        urls = []
        for submission in self.hot_submissions:
            urls.append(vars(submission)['url'])
        return '\n'.join(urls)
    
if __name__ == '__main__':
    reddit_top_programming = RedditHotTopics('funny')
    reddit_top_programming.fetch(limit=10)
    print(reddit_top_programming)