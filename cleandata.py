import pandas as pd

reviews_df = pd.read_csv("Dados/515k-hotel-reviews-data-in-europe/Hotel_Reviews.csv")
for i in reviews_df.columns:
	print(i)