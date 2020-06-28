import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Author,Book,Category
from auth.auth import AuthError, requires_auth

class LibraryTestCase(unittest.TestCase):
    """This class represents the library test case"""
    def setUp(self):
         """Define test variables and initialize app."""
         self.app = create_app()
         self.client = self.app.test_client
         self.database_name = "library_test"
         self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
         setup_db(self.app, self.database_path)
         self.admin='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZnbFFud3dmbDJBNDJLMkVOSUdKbSJ9.eyJpc3MiOiJodHRwczovL3B1YmxpY2xpYnJhcnkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjhlNzMyNzE0NjhjMDAxM2ZmYjNhNCIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTU5MzM3NTI2MiwiZXhwIjoxNTkzMzgyNDYyLCJhenAiOiI5VVhweUIycWhYQjQ4bDZmckNEaFBvZnJTWmpteWhmQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOltdfQ.c4K9G3WNC5M-ktTnUAdyOXEzaJgbA2G1ZPdGXP5HrFKBdMBt7YwuVikTQBxT3X_vL2rLtIDs72Lt9AGn0F56k2km1NrqYbvTqcoHizktnmyM1hRLMZFb-6kZ7pV3ZsTSM77Oa3pZHddZLVvid9z_y6NqjQ0qwHSlLwXNS_fRYOutwSGsAqvQ1gP5ME4HopEKgMQbpTfm-6FW_EsKEd1JDDJaJuK9sFTuFpkAw5iPT9w5LVbYujdUICov9DwtOQpVpBqolv26VaXrmmjTj0f4a2hw6S8nxSvTIkSuUblxGC1tprD0IPmrXhDa9Kc4TRNABeWBpbJLOhbRXJnursvv5A'
         self.author_assistant='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZnbFFud3dmbDJBNDJLMkVOSUdKbSJ9.eyJpc3MiOiJodHRwczovL3B1YmxpY2xpYnJhcnkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjhlNzA0NzE0NjhjMDAxM2ZmYjNhMSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTU5MzM3MjQ2MCwiZXhwIjoxNTkzMzc5NjYwLCJhenAiOiI5VVhweUIycWhYQjQ4bDZmckNEaFBvZnJTWmpteWhmQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicGF0Y2g6Ym9vayIsInBvc3Q6Ym9vayJdfQ.iuMOHrIhToz8LZ9eg9BmHl4XsP1tfzBJ_l23Jklgy7nXIXSmZBy8_McNpGM9IWL88IaIwW0VqxFTBbimKZ3bwRumPCrdnu4VU_fA7Xs_UKSg_MVgMZyxAuawz8kcy1X6M7BIHKAuQUxTjADrwBE_4c6J1EKU0dJaGxeqQY2u0yvy7r5zR92bvNo-9rDZheA3saeNu3lvUd1yXgsjkwDKr1qQSJSGiWW4XkUxFcwoOv7AOf4fnz_bjffIxBsw5W_jl2vgJe2QQzsv-bFC4No7YtILyiVYpIQKUxAGsgrMSkt9xZcgnf_r1FwGnsOK7t43X63Ly8TNzhUBXUWoh8Y2Nw'
        
         with self.app.app_context():
             self.db = SQLAlchemy()
             self.db.init_app(self.app)
             self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass
        
        ##test list book
    def test_get_book(self):
        res= self.client().get('/books')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['books'])
        self.assertTrue(data['book_total'])
        self.assertTrue(data['category'])

    #test delete book
    def test_delet_book(self):
        res = self.client().delete('/books/2', headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertEqual(data['massege'], 'book is delete')
    
    #test updat book with new values:
    def test_updat_book(self):
        res=self.client().patch('/books/3',headers={'Authorization': 'Bearer ' + self.author_assistant},json={ 'book_name':'Fish: A Proven Way to Boost Morale and Improve Results','book_issue':'2020-03-13'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['massege'], 'update the book')
        self.assertEqual(data['updated'], 3)
    
    #test create new book
    def test_create_book(self):
       res=self.client().post('/books', headers={'Authorization': 'Bearer ' + self.author_assistant},json={'book_name':'TestAuthor','book_issue':'22-3-2010'})
       data= json.loads(res.data)
       self.assertEqual(res.status_code, 200)
       self.assertEqual(data['success'], True)
       self.assertTrue(data['book'])
    
    def test_list_authore(self):
        res= self.client().get('/authors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['authors'])

    def test_delete_author(self):
        res = self.client().delete('/authors/2',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertEqual(data['massege'], 'Author is deleted')

    def test_updat_author(self):
        res=self.client().patch('/authors/3',headers={'Authorization': 'Bearer ' + self.admin}, json={ 'auth_nam':'Test','gender':'F','count_book':1})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_create_autor(self):
        res=self.client().post('/authors', headers={'Authorization': 'Bearer ' + self.admin} ,json={'auth_nam':'TestAuthor','gender':'F','count_book':1})
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['author'])

    def test_search_book(self):
        res=self.client().post('/books/search', json={"search":"Book3"})
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total'])
        self.assertTrue(data['total'])

    def test_404_if_delete_book_does_not_found(self):
        res = self.client().delete('/books/1000',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 200).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page Not Found')

    def test_404_if_delete_uthor_dos_not_found(self):
        res = self.client().delete('/authors/1000',headers={'Authorization': 'Bearer ' + self.admin})
        data = json.loads(res.data)
        auth = Author.query.filter(Author.id == 200).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page Not Found')

    def test_404_search_Non(self):
        res=self.client().post('/books/search', json={"search":""})
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page Not Found')
    

    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()