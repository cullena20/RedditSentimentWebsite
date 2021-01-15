import praw
import json
with open('config.json') as config_file:
    config_data = json.load(config_file)


def create_connection():
    reddit = praw.Reddit(client_id=config_data["client_id"],
                         client_secret=config_data["client_secret"],
                         user_agent=config_data["user_agent"])
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
