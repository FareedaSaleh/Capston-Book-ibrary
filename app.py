import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import Book,Author,setup_db,db

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  migrate = Migrate(app, db)
  CORS(app, resources={r"*": {"origins": "*"}})
  
  #CORS configration
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,PATCH,POST,DELETE,OPTIONS')
    return response
  
  @app.route('/books', methods=['GET'])
  def get_books():
    books = Book.query.all()
    books_formated=[book.format() for book in books]
    return jsonify({
       "success": True,
       "books":books_formated
    })
  
  #list the Authors
  @app.route('/authors', methods=['GET'])
  def get_authers():
    author=Author.query.all()
    author_formated=[auth.format() for auth in author]
    return jsonify({
       "success": True,
       "books":author_formated
    })
  
  
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
