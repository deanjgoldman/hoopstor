from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import listdir
import regex as re


app = Flask(__name__)

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)


class Blogpost(db.Model):
    __tablename__ = "blogpost"
    userid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    image = db.Column(db.Text)


def get_htmls():
    files = listdir(app.template_folder)
    return files


def get_context_data():
    context = {}
    texts = []
    indices = []
    files = get_htmls()
    for filename in files:
        if re.search('post', filename):
            regex_num = re.search(r'\d+', filename)
            filenumber = regex_num.group()
            index = regex_num.span()[0]
            html_text = filename[:index] + ' ' + filenumber
            texts.append(html_text)
            indices.append(filenumber)
    context["post"] = dict(zip(texts, indices))
    return context


@app.route('/')
def index():
    # context = None  # get_context_data()
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
