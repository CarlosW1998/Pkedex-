# Daga Mining Project-
The objective of this project is make a datamining on Twetter data. First a model is trained to predict if a sentence is positive or negative. 
For the training has used a dataset of 10000 twetts already classifieds, 5000 negatives and 5000 positives, to do the cleaningprocesse has used NLTK(Natural Language Tool kit).
After training the model, its necessary conect to Twetter API and get some twetts for analyse. In this step are necessary a twetter developer acount so we can conect to twiter and get twetts abou a thema, so we can analyse if the tweet about the themas are negative or positive.
# Run The Container
To start the docker container run the comands
> docker build -t senta:1.0 .
> docker run -p 8888:8888  senta:1.0
Open the link will apear in comand line in your browser and open the Main.ipynb 
Set the variables, and execute the code.