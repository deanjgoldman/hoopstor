from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)


class Blogpost(db.Model):
    __tablename__ = "blogpost"
    userid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    image = db.Column(db.Text)


@app.route('/')
def index():
    context = Blogpost.query.all()
    return render_template('index.html', context=context)


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
