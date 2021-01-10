from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_posts(posts):
    sia = SentimentIntensityAnalyzer()
    results = list()
    for post in posts:
        pol_score = sia.polarity_scores(post.title)
        pol_score['headline'] = post.title
        results.append(pol_score)
    return results


def sentiment_to_df(analyzed_posts):
    df = pd.DataFrame.from_records(analyzed_posts)
    return df


def label_df(df):
    df['label'] = 0  # creates label column
    df.loc[df['compound'] > 0.2, 'label'] = 1  # if compound score is greater than 0.2 we label it as positive
    df.loc[df['compound'] < -0.2, 'label'] = -1  # if compound score is less than -0.2 we label it as positive
    return df


# hopefully we can get this to work
def get_plot(sentiment_df):
    percentages = sentiment_df.label.value_counts(normalize=True) * 100
    ax = sns.barplot(x=percentages.index, y=percentages)
    ax.set(xlabel=['Negative', 'Neutral', 'Positive'], ylabel='Percentage')
    plt.savefig('plot.png')


def get_sentiment(sentiment_df):
    percentages = dict(sentiment_df.label.value_counts(normalize=True) * 100)
    # this didn't work :(
    # for key in percentages.keys():
    #     if key == -1:
    #         percentages['Negative'] = percentages[key]
    #         del percentages[key]
    #     if key == 0:
    #         percentages['Neutral'] = percentages[key]
    #         del percentages[key]
    #     if key == 1:
    #         percentages['Positive'] = percentages[key]
    #         del percentages[key]
    return percentages


def get_most_positive(df):
    pd.options.display.max_colwidth = 200
    sorted_df = df.sort_values(by='compound')
    most_positive = list(sorted_df.tail(5)['headline'])
    return most_positive


def get_most_negative(df):
    pd.options.display.max_colwidth = 200
    sorted_df = df.sort_values(by='compound')
    most_negative = list(sorted_df.head(5)['headline'])
    return most_negative
