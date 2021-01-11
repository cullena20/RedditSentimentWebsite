import machinelearning.redditapi as ra
import machinelearning.sentiment as se


def sentiment_analysis(sub):
    reddit = ra.create_connection()
    subreddit = ra.get_subreddit(reddit, sub)
    posts = ra.get_posts(subreddit)
    results = se.analyze_posts(posts)
    df = se.sentiment_to_df(results)
    labeled_df = se.label_df(df)
    most_positive = se.get_most_positive(df)
    most_negative = se.get_most_negative(df)
    # plot = se.get_plot(labeled_df)
    percentages = se.get_sentiment(labeled_df)
    return most_positive, most_negative, percentages
