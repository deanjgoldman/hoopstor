from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post' + str(post_id) + '.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/blogposts')
def blogposts():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
