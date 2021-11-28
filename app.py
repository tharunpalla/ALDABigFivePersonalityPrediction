from flask import Flask, render_template, request

app = Flask(__name__)

questions = ["I am the life of the party", "I feel little concern for others.", "I am always prepared.",
             "I get stressed out easily.", "I have a rich vocabulary.", "I don't talk a lot.",
             "I am interested in people.", "I leave my belongings around.", "I am relaxed most of the time.",
             "I have difficulty understanding abstract ideas.", "I feel comfortable around people.", "I insult people.",
             "I pay attention to details.", "I worry about things.", "I have a vivid imagination.",
             "I keep in the background.", "I sympathize with others' feelings.", "I make a mess of things.",
             "I seldom feel blue.", "I am not interested in abstract ideas.", "I start conversations.",
             "I am not interested in other people's problems.", "I get chores done right away.",
             "I am easily disturbed.", "I have excellent ideas.", "I have little to say.", "I have a soft heart.",
             "I often forget to put things back in their proper place.", "I get upset easily.",
             "I do not have a good imagination.", "I talk to a lot of different people at parties.",
             "I am not really interested in others.", "I like order.", "I change my mood a lot.",
             "I am quick to understand things.", "I don't like to draw attention to myself.",
             "I take time out for others.", "I shirk my duties.", "I have frequent mood swings.",
             "I use difficult words.", "I don't mind being the center of attention.", "I feel others' emotions.",
             "I follow a schedule.", "I get irritated easily.", "I spend time reflecting on things.",
             "I am quiet around strangers.", "I make people feel at ease.", "I am exacting in my work.",
             "I often feel blue.", "I am full of ideas."
             ]


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/quiz/short')
def get_short_quiz():  # put application's code here
    return render_template('shortquiz.html', questions=questions, count=0, start=0, end=10)


@app.route('/quiz/long')
def get_long_quiz():  # put application's code here
    return render_template('longquiz.html', questions=questions, count=0, start=0, end=50)


@app.route('/quiz')
def get_quiz():  # put application's code here
    return render_template('selectquiz.html')


@app.route('/quiz/result')
def get_result():  # put application's code here
    return render_template('result.html')


@app.route('/getdata', methods=['POST'])
def get_Data():
    if request.method == 'POST':
        data = request.form
        return data
    else:
        return "hellooo"


if __name__ == '__main__':
    app.run()
