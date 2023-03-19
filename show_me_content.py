from content_agg import RedditHotTopics, NewsSource
from email_content import sendEmail
query = 'six nations'

sources1 = RedditHotTopics(query)
sources2 = NewsSource(query)

content = sources1.__repr__() + "\n" + sources2.__repr__()

sendEmail(query,content)