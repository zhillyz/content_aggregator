from content_agg import RedditHotTopics, NewsSource
query = 'ukraine'

sources = RedditHotTopics(query)
print(sources)
sources = NewsSource(query)
print(sources)