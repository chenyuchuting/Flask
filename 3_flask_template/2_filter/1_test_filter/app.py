from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index/')
def index():
    context = {
        "users": ['Link1', 'Link2', 'Link3'],
        'ids': ['id1'],
        "person": {
            'username': 'Link1',
            'age': 18,
            'sex': 'man'
        },
        "books": [
            {
                'name': "杂谈",
                'author': '鲁迅',
                'code': '123'
            }, {
                'name': "生活的智慧",
                'author': '叔本华',
                'code': '124'
            }, {
                'name': "随笔",
                'author': '培根',
                'code': '125'
            }
        ],
    }
    # keys()->iterkeys
    # values()->itervalues
    # items()->iteritems
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()