import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_name = "library"
# url for local database:
database_path = "postgres://{}/{}".format('localhost:5432', database_name)
# database url for heroku
# database_path ='postgres://ayrojxosrdycfl:1879923d9fad9601ba959eea32940b7688
# '54f1f66a7b02a77818ab2678083dce@ec2-34-192-173-173.compute-1.amazonaws.com:5432/dfr9u71jrqqbdr'
db = SQLAlchemy()
# migrate = Migrate(app, db)

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)


'''
Author
'''


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(
        db.Integer().with_variant(
            Integer,
            "sqlite"),
        primary_key=True)
    auth_nam = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=True)
    count_book = db.Column(db.Integer, nullable=False)
    # category=db.relationship('Category', backref='author', lazy=True)

    def __init__(self, auth_nam, gender, count_book):
        self.auth_nam = auth_nam
        self.gender = gender
        self.count_book = count_book
        # self.category = category

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'auth_nam': self.auth_nam,
            'gender': self.gender,
            'count_book': self.count_book,
            # 'category': self.category
        }


'''
Books
'''


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(
        db.Integer().with_variant(
            Integer,
            "sqlite"),
        primary_key=True)
    # id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, nullable=False)
    book_issue = db.Column(db.DateTime, nullable=False)
    # category=db.relationship('Category', backref='book', lazy=True)
    # category=db.Column(db.String,nullable=True)

    def __init__(self, book_name, book_issue):
        db.create_all()
        self.book_name = book_name
        self.book_issue = book_issue
        #  self.category = category

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'book_issue': self.book_issue,
            # 'category': self.category,
        }


'''
Ralation with Category Book and Author
will be add in the 2nd version of this project
'''


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, nullable=False)
    # book_id = db.Column(db.Integer, db.ForeignKey('book.id'),nullable=False)
    # author_id = db.Column(db.Integer,
    # db.ForeignKey('author.id'),nullable=False)

    def __init__(self, name, book_id, author_id):
        self.name = name
        # self.book_id = book_id
        # self.author_id = author_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            # 'book_id': self.book_id,
            # 'author_id': self.author_id,
        }
