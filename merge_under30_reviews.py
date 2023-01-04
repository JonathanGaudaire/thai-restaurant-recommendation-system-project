import pandas as pd

reviews = pd.read_csv("D:\Documents\Travail\Mcgill\\5- Fall 2022\INSY 448 - Text and social media analytics\Code\Assignment 2\yelp_reviews.csv")
reviews = reviews[['restaurant_link','rating','review']]
reviews2 = reviews.groupby('restaurant_link').count()
reviews2 = reviews2.drop(reviews2[reviews2['rating'] < 30].index)
reviews3 = pd.merge(reviews2, reviews, how='left', on=['restaurant_link'])
reviews3 = reviews3.drop(columns=['rating_x','review_x'],axis=1)
reviews3.to_csv("D:\Documents\Travail\Mcgill\\5- Fall 2022\INSY 448 - Text and social media analytics\Code\Assignment 2\yelp_reviews_final.csv", index=False)
