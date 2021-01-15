import praw
import os

client_id = os.environ.get('client_id', None)
client_secret = os.environ.get('client_secret', None)
user_agent = os.environ.get('user_agent', None)


def create_connection():
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    return reddit


def get_subreddit(reddit, subreddit):
    subreddit = reddit.subreddits.search_by_name(subreddit, exact=True)[0]
    return subreddit


def get_posts(subreddit):
    posts = set()  # use a set to clear any duplicates
    for post in subreddit.new(limit=50):
        posts.add(post)
    posts = list(posts)  # easier to work with lists
    return posts
