from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your brouser is %s' % user_agent, 400 # подменяем код состояния на '400' :TEST


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


# редирект на другой ресурс :TEST
@app.route('/test')
def redir():
    return redirect('https://www.youtube.com/watch?v=y1edhgne48g')


if __name__ == '__main__':
    app.run(debug=True)
