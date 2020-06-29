import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Author, Book, Category
from auth.auth import AuthError, requires_auth
import datetime


class LibraryTestCase(unittest.TestCase):
    """This class represents the library test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "library_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.admin = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZnbFFud3dmbDJBNDJLMkVOSUdKbSJ9.eyJpc3MiOiJodHRwczovL3B1YmxpY2xpYnJhcnkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjhlNzMyNzE0NjhjMDAxM2ZmYjNhNCIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTU5MzQyODk2OCwiZXhwIjoxNTkzNDM2MTY4LCJhenAiOiI5VVhweUIycWhYQjQ4bDZmckNEaFBvZnJTWmpteWhmQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmF1dGhvciIsImRlbGV0ZTpib29rIiwicGF0Y2g6YXV0aG9yIiwicGF0Y2g6Ym9vayIsInBvc3Q6YXV0aG9yIiwicG9zdDpib29rIl19.yt4QrKXT5YKo6gadT-ZxpgD1AoUc12sbIy_nd9DBT0S208dQDd8ghUolSr6s1suw3R4sMl0EAJfe0C-u77w5MNJmf2GdclO5aybYuzz0Ohc3LiIVHbTohgrFengzhGUYV3fgX01QiKnw3NZ7IIZct0vfVKSG2z_fSbbnLGO7GPmpW8Kc1_Rr-LpN-YFUqpw50_oUiunhcJTxKSfIUfHbjcDAg1JJBYHWZl-M4OI-YNXwll805rzgwBZkWKW37Yihahg0-8GEhP2Mhb-9RK6hpv0EWRLOJw5h6tRFvWiT7UV3_Vd4ByCT7zQ4wDaKo9Wumze8UHKNCJXICAkpRTjEww'
        self.author_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZnbFFud3dmbDJBNDJLMkVOSUdKbSJ9.eyJpc3MiOiJodHRwczovL3B1YmxpY2xpYnJhcnkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjhlNzA0NzE0NjhjMDAxM2ZmYjNhMSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTU5MzQyOTAyMSwiZXhwIjoxNTkzNDM2MjIxLCJhenAiOiI5VVhweUIycWhYQjQ4bDZmckNEaFBvZnJTWmpteWhmQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicGF0Y2g6Ym9vayIsInBvc3Q6Ym9vayJdfQ.Ll4WqX0oUQm5pR-Mqrfixlp-AD913oL0AgPMqEH5OTch4BMAkHXSj8plNyNFJ7kj2InlzN9rfU9jgulZUWhQOFD4sTqQNHWTw1kVcW75kShZvkpaHafvctzCqZtyOKhfpdeMDiwXriaYdVPbQO7AIpojqTMfpr2jzXD5HQfRBNHIQ7884GR5CpJN0b_Bxy9ernjPT0BjXiRONCxt_H5CAA7smbVmIk49WFzNevuVf1UwPt7WPkpZWWLeLb6wRQ-IcmU1QTAHjbhAulQYHqB_d2hiqEI3MWrOVeTJYgvvdzrsphJv_NxitNu8M6w5WJwXcvbWR31ZuGO5PyQqLi1Yhg'

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

        # test list book
    def test_get_book(self):
        res = self.client().get('/books')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['books'])
        self.assertTrue(data['book_total'])
        self.assertTrue(data['category'])

    # test delete book
    def test_delet_book(self):
        res = self.client().delete('/books/2',
                                   headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertEqual(data['massege'], 'book is delete')

    # test updat book with new values:
    def test_updat_book(self):
        res = self.client().patch(
            '/books/4',
            headers={
                'Authorization': 'Bearer ' + self.author_assistant},
            json={
                'book_name': 'Fish: A Proven Way to Boost Morale and Improve Results',
                'book_issue': '2020-03-13'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['massege'], 'update the book')
        self.assertEqual(data['updated'], 4)

    # test create new book
    def test_create_book(self):
        new_book_issue = datetime.datetime(2020, 1, 1)
        res = self.client().post(
            '/books',
            headers={
                'Authorization': 'Bearer ' + self.author_assistant},
            json={
                'id': 11,
                'book_name': 'Hope every day',
                'book_issue': new_book_issue})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['book'])

    def test_list_authore(self):
        res = self.client().get('/authors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['authors'])

    def test_delete_author(self):
        res = self.client().delete('/authors/2',
                                   headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertEqual(data['massege'], 'Author is deleted')

    def test_updat_author(self):
        res = self.client().patch(
            '/authors/3',
            headers={
                'Authorization': 'Bearer ' + self.admin},
            json={
                'auth_nam': 'Test',
                'gender': 'F',
                'count_book': 1})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_create_autor(self):
        res = self.client().post(
            '/authors',
            headers={
                'Authorization': 'Bearer ' + self.admin},
            json={
                'auth_nam': 'TestAuthor',
                'gender': 'F',
                'count_book': 1})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['author'])

    def test_search_book(self):
        res = self.client().post('/books/search', json={"search": "Hope"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total'])
        self.assertTrue(data['total'])

    def test_404_if_delete_book_does_not_found(self):
        res = self.client().delete('/books/1000',
                                   headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 200).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page Not Found')

    def test_404_if_delete_uthor_dos_not_found(self):
        res = self.client().delete('/authors/1000',
                                   headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        auth = Author.query.filter(Author.id == 200).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page Not Found')

    # test Unuthorization:
    # book and uthor can delete by admin role.
    def test_401_if_uthors_delete_book(self):
        res = self.client().delete(
            'books/4',
            headers={
                'Authorization': 'Bearer ' + self.author_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_if_uthors_delete_authors(self):
        res = self.client().delete('authors/4',
                                   headers={'Authorization': 'Bearer ' + self.author_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_if_uthors_create_uthors(self):
        res = self.client().post(
            'authors',
            headers={
                'Authorization': 'Bearer ' + self.author_assistant},
            json={
                'auth_nam': 'TestAuthor',
                'gender': 'F',
                'count_book': 1})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_search_Non(self):
        res = self.client().post('/books/search', json={"search": ""})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page Not Found')



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
