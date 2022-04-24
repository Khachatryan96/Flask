from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primery_key=True)
    title = db.Column(db.String(100), nullabel=False)
    intro = db.Column(db.String(300), nullabel=False)
    text = db.Column(db.Text, nullabel=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/index')
def indx():
    return render_template('index.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f"User Page - {name  + ' ' 'id' + str(id)}"


if __name__ == '__main__':
    app.run(debug=True)