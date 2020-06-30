# Capston-Book-ibrary
# Capston project - Hope library api

## Getting Started

### Installing Dependencies

#### Python Python 3.6.9

In this project I use python 3.6.9. Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
This is the first version of the project so we just have simpel database structures,two tabels Books and authors. later the project will have category tabel and relation between the book and author tabels. 
With Postgres running, restore a database using the library.pgsql file provided. From the root folder in terminal run:
```bash
psql  library.pgsq < library.psql
```
######  Note: make sure to replace the database URL on the models.py and test.py
## Running the server

From within the `Booklibrary` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Rols

Hope library is online public library that anable every one to post thier free book so every one in the world can read it.
this is the first version of the project that just have simple database structre and also it have 2 rols:
- any one can list the book or search about book
- ##### Author assistant : 
   who can add or deit the book to the library
- ##### Admin
   who can add the outhors, edit or delete them in addation to the author assistan role
 ##### Permasions:
 - delete:author : To delete author		
 - delete:book   : To delete book from the book list
 - patch:author  : To edit author information
 - patch:book : To edit book information
 - post:author : To create new uathor
 - post:book   : To create new Book

## Endpoints
 ##### GET '/' 
  is the main route it represent 'Welcom'
 ##### GET '/books'
 - Not requerd any permation.
 - Fetches a dictionary of Book 
- Request Arguments: None
- Returns: An object  of book every 10 books on one page.


    {
    "book_total": 1,
    "books": [
        {
            "book_issue": "Fri, 13 Mar 2020 00:00:00 GMT",
            "book_name": "Computer11",
            "id": 1
        }
    ],
    "category": [],
    "success": true
}
##### POST '/book'
 - Requires permission post:book
 - Request Arguments: jwt and
 - post book as jeson boody

            {"book_name":"Fish: A Proven Way to Boost Morale and Improve 
            Results","book_issue":"2020-03-13"}
- it return json of book id and code status
##### PATCH '/books?page=<int>'
- Requires permission patch:book	
- edit book according to the argument book id and send the editing book as json body

      {"book_name":"Fish: A Proven Way to Boost Morale and Improve Results","book_issue":"2013-03-13"}
- Request Arguments: jwt,book_id 
- it return the json of book id
##### DELET '/books?page=<int>'
- Requires permission delete:book  
- Request Arguments: id,jwt
- delete book from book list according of specific book id 
- it returun json object of the book Id that is remove 

##### GET '/authors' 
- it's not requerd permission
- Request Arguments: None
- Retrive list of authors as json objec

         {
         "author_count": 1,
         "authors": [
          {
            "auth_nam": "Abdullah",
            "count_book": 2,
            "gender": "M",
            "id": 1
        }
         ],
      "success": true
        }
##### POST '/authors'
- Add new authors
- Requires permission post:author
- Request Argument:jwt and 
- send a json body of new authors

         {
            "auth_nam": "Abdullah",
            "count_book": 2,
            "gender": "M",
            "id": 5
        }
- Return: new author id

##### PATCH '/authors/?page=<int>'
 -  Requires permission patch:author	
 -  Edit existing author  with the specified author id 
 -  Request Argument id of author, jwt
 -  Return json of edit author id
 ##### DELETE '/authors/?page=<int>'
 -  Requires permission delete:author
 -  delete existing author  with the specified author id 
 -  Request Argument id of author, jwt
 -  Return json of deleted author id
##### POST '/books/search'
-  Search book based on “search” argument .It will return any bookss that contains “search” as a substring.
-  Request Argument: "search"
-  Return:a json object that includes a list of books that match the substring argument request, total (total number of matchedbooks)

             ##request
             {
             "search":"fish"
                 
             }
             ##response
             
                        {
            "result": [
              {
            "book_issue": "Fri, 13 Mar 2020 00:00:00 GMT",
            "book_name": "Fish: A Proven Way to Boost Morale and Improve Results",
            "id": 3
             }
          ],
             "success": true,
             "total": 1
            }

### Error Handling
Errors are returned as JSON objects in the following format:
  
  {
    "success": False, 
    "error": 400,
    "message": "Bad Request"
      
  }
 - 400 – bad request 
 - 401 - not authorized 
 - 404 – resource not found 
- 422 – unprocessable 
- 500 - internal server error

## Testing
To run the tests, run

    dropdb library_test
    createdb library_test
    psql library_test < library.psql
    python3 test_app.py
## Heroku :
The application is build and deploy on Herku
- http://hope-library1.herokuapp.com

## Token :
admin = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZnbFFud3dmbDJBNDJLMkVOSUdKbSJ9.eyJpc3MiOiJodHRwczovL3B1YmxpY2xpYnJhcnkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjhlNzMyNzE0NjhjMDAxM2ZmYjNhNCIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTU5MzUzNjU2NiwiZXhwIjoxNTkzNjIyOTY2LCJhenAiOiI5VVhweUIycWhYQjQ4bDZmckNEaFBvZnJTWmpteWhmQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmF1dGhvciIsImRlbGV0ZTpib29rIiwicGF0Y2g6YXV0aG9yIiwicGF0Y2g6Ym9vayIsInBvc3Q6YXV0aG9yIiwicG9zdDpib29rIl19.iXZQJENKo-aZRaV6tDjwDw95oPTOSV6VCYzzQXty6w7X3C_BRpIbeW1rZqu04UXroqUvrt4ABVpK_fhboJk4pK1EtSpgNy4JBAIirKnI-PNYP0j_7Bu_uihUxhzC1WtutPlp1SUgJZS8Z0vLNN3W7EK2Y56UhYUcQIDTw8c6gtsHvachcbDihrd4OcjsESMCSPTngug1Mk9IHZ7-x-zzs9CsF4NG2X7DRztVmDi7ql1lPd74TKqTMBuwnk-BQH9DU61N0APoob4RMgjPHQOojo1-GNW9g7-Dm7eIawH1AfLksVlh0INiynF8MLDxJm-oGMPq2kRTu64q2VBucFAq6A'

author_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZnbFFud3dmbDJBNDJLMkVOSUdKbSJ9.eyJpc3MiOiJodHRwczovL3B1YmxpY2xpYnJhcnkudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjhlNzA0NzE0NjhjMDAxM2ZmYjNhMSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTU5MzUzNjY1MCwiZXhwIjoxNTkzNjIzMDUwLCJhenAiOiI5VVhweUIycWhYQjQ4bDZmckNEaFBvZnJTWmpteWhmQSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicGF0Y2g6Ym9vayIsInBvc3Q6Ym9vayJdfQ.qNQ3VoXfq_dqjAdvitLEzqCwG3Yx6MwtFQNs2qESz5licRPwnUowUImn4onz5HBKPHTaC8_ra3XVlOVeeZw1pLp3_YhEDbhLStiNGLkvGP6rqf_bdCKVgUYA3tUdTJI6jEOjxKPNWod96bgJhNcp1DLahTVisG3fDdWlHabZ5kV0N38qCx0dYvgPKE_Mwgo6yVwB1lnrPEFYsWHn1rW_vg18WPEnsbkuyiUre29Hn8cwg-qeA_xWnEAf5_s30EQpjKEUOhDGiJU2U17_TmlF08eAl-PnPtoMehIR_ENnyhtdyKi03gbJqcfHGbkvjPdrDLDhbn2FJeO-r83QhMn6Ng'
