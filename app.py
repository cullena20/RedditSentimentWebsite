from flask import Flask, request, render_template
from machinelearning.mainml import sentiment_analysis
from prawcore.exceptions import NotFound, Forbidden, ResponseException
from boto.s3.connection import S3Connection

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        subreddit = request.form["subreddit"]
        try:
            most_positive, most_negative, percentages = sentiment_analysis(subreddit)
        except NotFound or Forbidden or ResponseException:
            error = "Subreddit does not exist. Please try again."
            return render_template('main.html', error=error)
        except IndexError:
            error = "Please enter a subreddit to analyze."
            return render_template('main.html', error=error)
        return render_template('main.html',
                               positive=most_positive,
                               negative=most_negative,
                               percentages=percentages)
    else:
        return render_template('main.html')
