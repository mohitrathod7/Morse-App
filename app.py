from flask import *
from morse import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/convert', methods=['get'])
def convert():
    answer = "|"
    og_text = request.args.get('text')
    text = og_text.lower()

    for eachLetter in text:
        if len(text) == 1:
            answer = answer + morse_code.get(eachLetter) + letter_space
        else:
            nextLetterIndex = text.index(eachLetter) + 1
            if nextLetterIndex >= len(text):
                nextLetter = ""
            else:
                nextLetter = text[nextLetterIndex]
                
            if eachLetter in morse_code and (nextLetter in text == " "):
                answer = answer + morse_code.get(eachLetter) + word_space
            else:
                answer = answer + morse_code.get(eachLetter) + letter_space
    return render_template('home.html', _answer=answer, _text=og_text)


@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug = True)
