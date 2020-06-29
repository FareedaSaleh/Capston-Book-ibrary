import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import Book, Author, Category, setup_db, db
from auth.auth import AuthError, requires_auth
from sqlalchemy import exc


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app, resources={r"*": {"origins": "*"}})

    # CORS configration
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    def paginate_book(request, selection):
        BOOK_PER_PAGE = 10
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * BOOK_PER_PAGE
        end = start + BOOK_PER_PAGE
        books = [book.format() for book in selection]
        current_book = books[start:end]
        return current_book

    def paginate_author(request, selection):
        AUTHOR_PER_PAGE = 10
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * AUTHOR_PER_PAGE
        end = start + AUTHOR_PER_PAGE
        authors = [auth.format() for auth in selection]
        current_author = authors[start:end]
        return current_author
# Book Routs

    @app.route('/books', methods=['GET'])
    def get_books():
        books = Book.query.all()
        total_book = len(books)
        categories = Category.query.all()
        category_formatted = [cat.format() for cat in categories]
        if total_book == 0:
            abort(404)
        book_list = paginate_book(request, books)
        return jsonify({
            "success": True,
            "books": book_list,
            "book_total": total_book,
            "category": category_formatted
        })

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    @requires_auth('delete:book')
    def delete_book(jwt, book_id):
        book = Book.query.filter(Book.id == book_id).one_or_none()
        if book is None:
            abort(404)
        else:
            book.delete()
        return jsonify({
            "success": True,
            "massege": 'book is delete',
            "deleted": book_id
        })

    @app.route('/books', methods=['POST'])
    @requires_auth('post:book')
    def create_book(jwt):
        new_book_name = request.json.get('book_name')
        new_book_issue = request.json.get('book_issue')

        if new_book_name is None or new_book_issue is None:
            print("Error - ", ex)
            abort(400)
        try:
            book = Book(book_name=new_book_name, book_issue=new_book_issue)
            book.insert()
            return jsonify({
                'success': True,
                'book': book.id
            })
        except BaseException as ex:
            print("Error - ", ex)
            abort(422)

    @app.route('/books/<int:book_id>', methods=['PATCH'])
    @requires_auth('patch:book')
    def edite_book(jwt, book_id):
        try:
            book = Book.query.filter(Book.id == book_id).one_or_none()
            body = request.get_json()
            book.book_name = body.get('book_name', None)
            book.book_issue = body.get('book_issue', None)

            book.update()
            return jsonify({
                "success": True,
                "massege": "update the book",
                "updated": book.id
            })
        except BaseException:
            abort(422)

# Author routs
    @app.route('/authors', methods=['GET'])
    def get_authers():
        author = Author.query.all()
        total_author = len(author)
        if total_author == 0:
            abort(404)
        author_list = paginate_author(request, author)
        return jsonify({
            "success": True,
            "authors": author_list,
            "author_count": total_author
        })

    @app.route('/authors/<int:auth_id>', methods=['DELETE'])
    @requires_auth('delete:author')
    def delete_uthor(jwt, auth_id):
        author = Author.query.filter(Author.id == auth_id).one_or_none()
        if author is None:
            abort(404)
        else:
            author.delete()
        return jsonify({
            "success": True,
            "massege": "Author is deleted",
            "deleted": author.id
        })
    # admin can only add the uthor

    @app.route('/authors/<int:auth_id>', methods=['PATCH'])
    @requires_auth('patch:author')
    def edite_author(jwt, auth_id):
        try:
            author = Author.query.filter(Author.id == auth_id).one_or_none()
            body = request.get_json()
            author.auth_nam = body.get('auth_nam', None)
            author.gender = body.get('gender', None)
            author.count_book = body.get('count_book', None)

            author.update()
            return jsonify({
                "success": True,
                "massege": 'Author updated',
                "updated": author.id
            })
        except BaseException:
            abort(422)

    @app.route('/authors', methods=['POST'])
    @requires_auth('post:author')
    def create_author(jwt):
        new_auth_name = request.json.get('auth_nam')
        new_gender = request.json.get('gender')
        new_count_book = request.json.get('count_book')

        if new_auth_name is None or new_gender is None or new_count_book is None:
            abort(400)
        try:
            author = Author(
                auth_nam=new_auth_name,
                gender=new_gender,
                count_book=new_count_book)
            author.insert()
            return jsonify({
                "success": True,
                "author": author.id
            })
        except BaseException:
            abort(422)

       # search endpont for book name
    @app.route('/books/search', methods=['POST'])
    def book_search():
        body = request.get_json()
        search = body.get('search', None)
        if search is None or search == '':
            abort(404)
        try:
            result = Book.query.order_by(
                Book.id).filter(
                Book.book_name.ilike(
                    '%{}%'.format(search))).all()
            book = [b.format() for b in result]
            total_search = len(book)

            return jsonify({
                "success": True,
                "result": book,
                "total": total_search
            })
        except BaseException:
            abort(422)

       # error handeler methods:
    @app.errorhandler(401)
    def unauthorized_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Page Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(500)
    def server_erorr(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Server Errore"
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code
    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
