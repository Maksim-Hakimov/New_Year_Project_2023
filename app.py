from flask import Flask, render_template, request, redirect
from utils import create_dict, load_json

template_folder = 'templates'

app = Flask(__name__)


@app.route('/')
def index():
    text = load_json()[-1].get('text')
    wish_list = load_json()

    if len(wish_list) <= 10:
        texts = wish_list
    else:
        texts = wish_list[:-10: -1]

    return render_template('index.html', text=text, texts=texts)


@app.route('/new_congratulation', methods=['POST'])
def new_congratulation():
    user = request.form.get('user_name')
    text = request.form.get('congratulation')

    create_dict(user, text)
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run(port=8001)
