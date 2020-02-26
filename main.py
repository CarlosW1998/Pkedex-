from nltk.corpus import twitter_samples
from util import remove_noise, get_tweets_for_model
from nltk.corpus import stopwords
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import random

#Words the must be removed
stop_words = stopwords.words('english')
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

train_data = dataset[:7000]
test_data = dataset[7000:]


print("Traaining Models...")
classifier = NaiveBayesClassifier.train(train_data)

print("Accuracy is:", classify.accuracy(classifier, test_data))

print("Ookay")

custom_tweet = "I ordered just once from TerribleCo, they screwed up, never used the app again."

custom_tokens = remove_noise(word_tokenize(custom_tweet))

print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))