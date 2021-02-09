import machinelearning.redditapi as ra
import machinelearning.sentiment as se


def sentiment_analysis(sub):
    # creates reddit connection and accesses subreddit
    reddit = ra.create_connection()
    subreddit = ra.get_subreddit(reddit, sub)
    # returns list of 50 most recent posts from the subreddit
    posts = ra.get_posts(subreddit)
    # uses VADER to analyze posts and returns list containing post headline and sentiment
    results = se.analyze_posts(posts)
    # converts results list to pandas dataframe
    df = se.sentiment_to_df(results)
    # converts sentiment scores to sentiments (1 for positive, 0 for neutral, -1 for negative)
    labeled_df = se.label_df(df)
    # gets most five most positive and five least positive headlines
    most_positive = se.get_most_positive(df)
    most_negative = se.get_most_negative(df)
    # creates percentages of positive, neutral, and negative posts from dataframe
    percentages = se.get_sentiment(labeled_df)
    return most_positive, most_negative, percentages
