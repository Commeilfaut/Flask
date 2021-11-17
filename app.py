from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'About page'


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page:' + name + " - " + str(id)


if __name__ == '__main__':
    app.run(debug=True)