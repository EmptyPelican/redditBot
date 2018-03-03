
# Pelican_Bot
import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("funny")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("secure_media: ", submission.secure_media)
    print("secure_media_embed: ", submission.secure_media_embed)
    print("---------------------------------\n")