from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import random
import pickle
from src.util import remove_noise, get_tweets_for_model

class SentimentalAnalyses():
    def __init__(self):
        self.model = None
        self.train_data = []
        self.test_data = []

    def trianModel(self, leng='english'):
        stop_words = stopwords.words(leng)
        print("Load Data... ", end='')
        positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
        negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')
        print("Ookay")

        print("Clear Data... ", end='')
        positive_cleaned_tokens_list = [remove_noise(token, stop_words) for token in positive_tweet_tokens]
        negative_cleaned_tokens_list = [remove_noise(token, stop_words) for token in negative_tweet_tokens]
        print("Ookay")

        print("Prepare for Model... ")
        positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
        negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

        positive_dataset = [(tweet_dict, "Positive") for tweet_dict in positive_tokens_for_model]
        negative_dataset = [(tweet_dict, "Negative") for tweet_dict in negative_tokens_for_model]

        dataset = positive_dataset + negative_dataset

        random.shuffle(dataset)

        self.train_data = dataset[:7000]
        self.test_data = dataset[7000:]


        print("Traaining Models...", end='')
        self.model =  NaiveBayesClassifier.train(self.train_data)
        print("Ookay")

    def getAcuracy(self):
        return  classify.accuracy(self.model, self.test_data)
    
    def save(self, path='Classify.pickle'):
        f = open(path, 'wb')
        pickle.dump(self.model, f)
        f.close()
    
    def load(self, path=''):
        f = open(path, 'rb')
        self.model = pickle.load(f)
        f.close()

    
    def predict(self, data, many=False):
        if not self.model:
            return "No Model Provide"
        if not many:
            data = [data]
        result = []
        
        for i in data:
            custom_tokens = remove_noise(word_tokenize(i))
            result.append(self.model.classify(dict([token, True] for token in custom_tokens)))
        return result

