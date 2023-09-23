import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    stringid=random.randrange(0, 4)
    sentence1="Logic will get you from A to B. Imagination will take you everywhere."
    sentence2="There are 10 kinds of people. Those who know binary and those who don't."
    sentence3="There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies."
    sentence4="It's not that I'm so smart, it's just that I stay with problems longer."
    sentence5="It is pitch dark. You are likely to be eaten by a grue."
    sentences=[sentence1,sentence2,sentence3,sentence4,sentence5] 
    selectedsentence=sentences[stringid]
    return render_template('index.html',selectedsentence=selectedsentence)