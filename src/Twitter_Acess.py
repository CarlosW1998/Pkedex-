import tweepy

class Acess():
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret):
        #Variables that contains the user credentials to access Twitter API 
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        # Creating the authentication object
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        # Setting your access token and secret
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        # Creating the API object while passing in auth information
        self.api = tweepy.API(self.auth) 
    
    def search(self, query=[], lang=["en"], count=100):
        if not query:
            return "No querry Provided"
        # Calling the user_timeline function with our parameters
        results = self.api.search(q=query, lang=lang, count=count)
        tweets = []
        # foreach through all tweets pulled
        for tweet in results:
            # printing the text stored inside the tweet object 
            tweets.append(tweet.text)
        return tweets

