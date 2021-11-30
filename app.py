import os

from flask import Flask, render_template, request

import score_calculator1
import score_calculator

image_path = os.path.join('..\static', 'images')

app = Flask(__name__)

short_questions= ["I am the life of the party",
                    "I am quiet around strangers.",
                  "I am relaxed most of the time.",
"I get irritated easily.",
"I sympathize with others' feelings.",
"I am not interested in other people's problems.",
"I follow a schedule.",
"I make a mess of things.",
              "I have a vivid imagination.",
              "I am not interested in abstract ideas.",

             ]
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
    print("len of sa", len(short_questions))
    return render_template('shortquiz.html', questions=short_questions, count=0, start=0, end=10)


@app.route('/quiz/long')
def get_long_quiz():  # put application's code here
    return render_template('longquiz.html', questions=questions, count=0, start=0, end=50)


@app.route('/quiz')
def get_quiz():  # put application's code here
    return render_template('selectquiz.html')


@app.route('/getdata', methods=['POST'])
def get_Data():
    if request.method == 'POST':
        data = request.form.to_dict()
        output = score_calculator.calculate_score(data)
        image_filename = os.path.join(image_path, 'alda.png')
        return render_template('result.html', image_in_base64=image_filename, output=output)


@app.route('/getdata_short', methods=['POST'])
def get_Data_short():
    if request.method == 'POST':
        data = request.form.to_dict()
        output = score_calculator1.calculate_score(data)
        image = ""
        if output == 4:
            image = "joey.jpg"
        elif output == 3:
            image = "sheldon.jpg"
        elif output == 2:
            image = "sherlock.jpg"
        else:
            image = "bb.jpg"
        image_filename = os.path.join(image_path, image)
        trait = "Big 5 personalities"
        return render_template('result_short.html', image_in_base64=image_filename, output=output, trait=trait)

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)
