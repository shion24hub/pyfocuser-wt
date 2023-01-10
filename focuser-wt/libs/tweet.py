import tweepy

from libs.config import (
    ACCESS_LEVEL,
    MY_ACCOUNT_ID,
    API_KEY,
    API_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    BEARER_TOKEN,
)

# with Tweepy v2
class v2 :
    def clientInfo4v2(self) :
        client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
        )
        return client

    def createTweet4v2(self, message) :
        tweet = self.clientInfo4v2().create_tweet(text=message)
        return tweet

# with Tweepy v1.1
class v11 :
    def createTweet4v11(self, message) :
        pass
    def createTweetWithMedia4v11(self) :
        pass

