from content_agg import RedditHotTopics, NewsSource
from email_content import sendEmail
from dotenv import load_dotenv
import os
load_dotenv()
CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')
NEWS_API = os.environ.get('NEWS_API')

query = '"six nations"'

sources1 = RedditHotTopics(query)
sources2 = NewsSource(query)

content = 'Reddit: \n' + sources1.__repr__() + "\nNewsAPI: \n" + sources2.__repr__()

sendEmail(query,content)