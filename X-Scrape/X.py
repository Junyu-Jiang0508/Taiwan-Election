import tweepy
import pandas as pd
from datetime import datetime

# Twitter API credentials
consumer_key = 'ImXjiRq6PksNoHvY8tSZGUm6j'
consumer_secret = 'IUr2nbftqwiWLZ09K9qcz0dzmh2lwlTDQS08IxpF3N27yQuS64'
access_token = '1405058071030861826-92kX8QNBDq5PBcF2sKT9tbje7xsvpg'
access_token_secret = 'PDqCJvi7H8HhVVe2wjTdgpCz9gItf6j1XwsByPVK9iaNV'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Define the user handles of the candidates
candidates = ['ChingteLai', 'KP_Taiwan', 'houyuih', 'bikhim', 'skchao2024']

# Define the time range
start_date = '2023-01-01'
end_date = '2024-01-13'

# Loop through each candidate and collect their tweets
for candidate in candidates:
    tweets_data = []
    tweets = tweepy.Cursor(api.user_timeline, screen_name=candidate, tweet_mode='extended').items()

    for tweet in tweets:
        tweet_date = tweet.created_at.strftime('%Y-%m-%d')
        if start_date <= tweet_date <= end_date:
            tweets_data.append({'date': tweet_date, 'content': tweet.full_text})

    # Convert to DataFrame and save to CSV
    if tweets_data:  # Check if there are any tweets
        df = pd.DataFrame(tweets_data)
        df.to_csv(f'{candidate}_tweets.csv', index=False)

print("Tweets have been saved to individual files.")
