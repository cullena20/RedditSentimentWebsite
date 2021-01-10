from flask import Flask, request, render_template
from machinelearning.main import sentiment_analysis
from prawcore.exceptions import NotFound, Forbidden

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        subreddit = request.form["subreddit"]
        try:
            most_positive, most_negative, percentages = sentiment_analysis(subreddit)
        except NotFound or Forbidden:
            error = True
            return render_template('main.html', error=error)
        return render_template('main.html',
                               positive=most_positive,
                               negative=most_negative,
                               percentages=percentages)
    else:
        return render_template('main.html')
