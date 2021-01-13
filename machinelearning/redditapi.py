import praw


def create_connection():
    reddit = praw.Reddit(client_id='<your client_id>,
                         client_secret='<your client_secret>',
                         user_agent='<your user-agent>')
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
