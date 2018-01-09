from bs4 import BeautifulSoup
from app import app, db, Blogpost
import regex as re
from os import listdir


def main():
    db.drop_all()
    db.create_all()
    files = listdir(app.template_folder)
    for html in files:
        if re.search('post', html):
            with open(app.template_folder + '/' + html, 'r') as html_doc:
                soup = BeautifulSoup(html_doc.read(), 'html.parser')
                title = soup.find('div', {"id": "title"}).h1.text
                author = soup.find('span', {"id": "author"}).text
                src = soup.find('img', {"id": "main"}).get('src')
            post = Blogpost(title=title, author=author, image=src)
            db.session.add(post)
            db.session.commit()
