from flask import Flask, request, render_template
from machinelearning.main import sentiment_analysis


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def adder_page():
    if request.method == "POST":
        subreddit = request.form["subreddit"]
        most_positive, most_negative, percentages = sentiment_analysis(subreddit)
        # percentages is dict
        return render_template('main.html',
                               positive=most_positive,
                               negative=most_negative,
                               percentages=percentages)
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
