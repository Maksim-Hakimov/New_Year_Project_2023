from flask import Flask, render_template
from utils import advent

template_folder = 'templates'

app = Flask(__name__)


@app.route('/')
def advent_time():
    time = advent()
    return render_template('index.html', time=time)


if __name__ == '__main__':
    app.run(port=8001)
