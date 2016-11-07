# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
    can print out a success/failure message if you want to.""")

import tweepy
import nltk
import requests
import requests_oauthlib

access_token = "717850987747270657-zD44jE2VIqJUIWyuoVF4yaXVaTgVrK3"
access_token_secret = "1Ju0siuUzyKXlMY759ZQUUZ2cvXwUxdPgDm4oMEBmZnx9"
consumer_key = "0Lh7G2arIpujbFpOj7B7ydUmr"
consumer_secret = "IU86PONny05mTpo4Y0C32O3CrHcTm3rM0B3fdmmH888XItvWC4"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
img = "C:/Users/Ben/Desktop/206/SI206/Homework3/media/pic.jpg"
api.update_with_media(img, status="#UMSI-206 #Proj3")
print("posted")