from flask import Flask, render_template, request, redirect
from utils import create_dict, load_json
import random

template_folder = 'templates'

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# Главна страница сайта
@app.route('/')
def index():
    """Передаю в переменную последнее введенное сообщение из функции загрузки json
       сохраняю список json в переменную
    """
    text = load_json()[-1].get('text')
    wish_list = load_json()

    if len(wish_list) <= 9:
        texts = wish_list
    else:
        # печатаю случайные 9 сообщений из списка словарей в переменную
        texts = random.sample(wish_list, 9)

    # Возвращаю путь к файлу html и назначаю переменные, которые буду использовать в html
    return render_template('index.html', text=text, texts=texts)


# Страница, передающая введенные пользователем данные
@app.route('/new_congratulation', methods=['POST'])
def new_congratulation():
    """
    user - принимает введенное пользователем значение, в поле user, с сайта
    text - принимает введенное пользователем значение, в поле text, с сайта
    """
    user = request.form.get('user_name')
    text = request.form.get('congratulation')

    # Вызываю функцию, которая добавляет новые данные в словарь json,
    create_dict(user, text)
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run(port=8001)
