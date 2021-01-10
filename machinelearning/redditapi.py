import praw


def create_connection():
    reddit = praw.Reddit(client_id='etCTL0OgGAY1jA',
                         client_secret='vMtYIGE5WVK8BDczKh7ZnRup3rb3ew',
                         user_agent='Conscious-Reply-7037')
    return reddit


def get_subreddit(reddit, subreddit):
    subreddit = reddit.subreddits.search_by_name(subreddit, exact=True)[0]
    return subreddit


# def get_subreddit(reddit):
#     while True:
#         u_sub = input('Type a subreddit to analyze: ')
#         try:
#             subreddit = reddit.subreddits.search_by_name(u_sub, exact=True)[0]
#             print()
#             return subreddit
#         except NotFound:
#             print("Subreddit does not exist! Please try again.")
#             continue
#         except ResponseException:
#             print("Could not access subreddit! Please try again")
#             continue


def get_posts(subreddit):
    posts = set()  # use a set to clear any duplicates
    for post in subreddit.new(limit=50):
        posts.add(post)
    posts = list(posts)  # easier to work with lists
    return posts


# def get_posts(subreddit):
#     try:
#         posts = set()  # use a set to clear any duplicates
#         for post in subreddit.new(limit=50):
#             posts.add(post)
#         posts = list(posts)  # easier to work with lists
#         return posts
#     except NotFound:
#         print("Subreddit does not exist! Please try again.")
#         sys.exit(1)
#     except Forbidden:
#         print("Could not access subreddit! Quitting program.")
#         sys.exit(1)
