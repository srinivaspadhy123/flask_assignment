from flask import Flask,request,jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from book_model import Book
from exceptions import RecordNotFoundException,build_exception_response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1/postgres'
db = SQLAlchemy(app)

@app.route("/add_book",methods=['POST'])
def add_book():
    data = request.get_json()
    book_id = data['book_id']
    book_title = data['title']
    book_author = data['author']
    try:
        query = text(f"INSERT INTO book_table(book_id,book_title,book_author) VALUES('{book_id}','{book_title}','{book_author}')")
        db.session.execute(query)
        db.session.commit()
        return "Book Details Successfully added"
    except Exception as exp:
        return {'status':500,
                'body':json.dumps(build_exception_response(exp))}
    finally:
        db.session.close()
    

@app.route("/view_book",methods=['GET'])
def view_book():
    try:
        query = text("SELECT * FROM book_table")
        response = db.session.execute(query)
        if not response:
            raise RecordNotFoundException(404,"Data Exception Ocurred..!!",{'errorMessage':'No Record Found with the given input'})
        result = [Book(row.book_id,row.book_title,row.book_author)for row in response]
        books = [{'book_id':book.get_book_id(),'book_title':book.get_title(),'book_author':book.get_author()} for book in result]
        return jsonify(books)
    except RecordNotFoundException as exp:
        return {'status':404,
                'body':json.dumps(exp.to_dict())}
    except Exception as exp:
        return {'status':500,
                'body':json.dumps(build_exception_response(exp))}
    finally:
        db.session.close()
    
@app.route("/update_book",methods=['PATCH'])
def update_book():
    try:
        book_id = request.args.get('book_id')
        update_details = request.get_json()
        title = update_details['title']
        author = update_details['author']
        fetch_query = text(f"SELECT * FROM book_table WHERE book_id='{book_id}'")
        fetch_response = db.session.execute(fetch_query).fetchone()
        if not fetch_response:
            raise RecordNotFoundException(404,"Data Exception Ocurred..!!",{'errorMessage':'No Record Found with the given input'})
        query = text(f"UPDATE book_table SET book_title='{title}',book_author='{author}' WHERE book_id='{book_id}'")
        db.session.execute(query)
        db.session.commit()
        return "Book Record Successfully Updated"
    except RecordNotFoundException as exp:
        return {'status':404,
                'body':json.dumps(exp.to_dict())}
    except Exception as exp:
        return {'status':500,
                'body':json.dumps(build_exception_response(exp))}
    finally:
        db.session.close()

@app.route("/delete_book",methods=['DELETE'])
def delete_book():
    book_id = request.args.get('book_id')
    title = request.args.get('title')
    try:
        fetch_query = text(f"SELECT * FROM book_table WHERE book_id='{book_id}',book_title='{title}'")
        fetch_response = db.session.execute(fetch_query).fetchone()
        if not fetch_response:
            raise RecordNotFoundException(404,"Data Exception Ocurred..!!",{'errorMessage':'No Record Found with the given input'})       
        query = text(f"DELETE from book_table WHERE book_id='{book_id}',book_title='{title}'")    
        db.session.execute(query)
        db.session.commit()
        db.session.close()
        return "Record Successfully Deleted"
    except RecordNotFoundException as exp:
        return {'status':404,
                'body':json.dumps(exp.to_dict())}
    except Exception as exp:
        return {'status':500,
                'body':json.dumps(build_exception_response(exp))}
    finally:
        db.session.close()
    