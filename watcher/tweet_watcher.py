# coding:utf-8
from twitter import *

class TweetWatcher:
    def __init__(self, keys):
        auth = OAuth(keys['access_token'], keys['access_token_secret'],
                keys['consumer_key'], keys['consumer_secret'])
        self.twitter_stream = TwitterStream(
                auth = auth,
                domain = 'userstream.twitter.com'
        )
        self.iterator = self.twitter_stream.statuses.sample()

    def watch(self):
        for status in self.twitter_stream.user():
            text = status.get('text')
            if isinstance(text, type(None)) is not True:
                if text.find('@mktakuya') is not -1:
                    print('Notice')

