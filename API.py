#Q.1- What is an access token?
'''
An access code is an object that describes the security context of a process or thread.

#Generate your access token for any API.(for example Twitter,Spotify etc)?

sign in to developer account.
create a new API.
under that go to keys and access token.
generate access token.

#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.

google IP address=172.217.15.68
facebook IP address=31.13.69.230

'''
#Q.3- Using Tweepy library try to extract tweets from Twitter.

from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy

oauth =tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("#arijitians"))

user=api.get_user('VivekSi75568633')
print(user.screen_name)
print(user.followers_count)


#Q.4 - What is a difference between library and API.Figure it out with examples.
'''
API is a part of library which defines how an application communicates with external code.
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.



#Q.5 - Try to access Spotify API.Find out some library for it and play some music.

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key ="zxoJ8wxViKF2eZ4PDDCov4Zgm"
consumer_secret ="PNza9CQUEcxV9JqigIdmtRRwIalPS8JfKBwBodQcLEQ9KS8iuS"
access_token ="1009290828563410945-ptWVq6QsNttoYdf00nlIqm8ySnuZMW"
access_secret ="b4vdi1IsREWWvTTj00ZZ5JxPDnGEqBtsVinUb4Ov0s5Ht"

class listener(StreamListener):
    def on_data (self,data):
        print(data)
        return True
    def on_error (self,status):
        print(status)
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["arijit singh"])









