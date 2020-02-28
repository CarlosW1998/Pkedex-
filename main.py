from src.Twitter_Acess import Acess
from src.Analyses import SentimentalAnalyses
import matplotlib.pyplot as plt
import numpy as np
import sys


path = "model.pickle"
print(sys.argv[1:])
api = Acess(*sys.argv[1:])
model = SentimentalAnalyses()
model.load(path=path)



while True:
    print(">>>", end='')
    i = input()
    if i == 'exit':
        break
    opertion = list(i.split())
    if opertion[0] == 'search':
        #try: 
        process = api.search(list(opertion[2].split('-')), count=opertion[1])
        response = model.predict(process, many=True)
        label = ['Positive', 'Nevative']
        data = [response.count('Positive'), response.count('Negative')]
        index = np.arange(len(label))
        plt.bar(index, data)
        #plt.xlabel('Genre', fontsize=5)
        plt.ylabel('No of Twetts', fontsize=5)
        plt.xticks(index, label, fontsize=5, rotation=30)
        plt.title('Search for ' + opertion[2])
        plt.show()
            
        #except:
            #print("Invalid Input")
    else:
        print("Invalid Input")

