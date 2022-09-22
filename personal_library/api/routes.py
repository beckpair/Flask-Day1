import json
from flask import Blueprint, request, jsonify
from personal_library.models import db, Book, book_schema, books_schema
from personal_library.helpers import token_required

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return{'some': 'value'}

@api.route('/books', methods = ['POST'])
@token_required
def create_book(current_user_token):
    author = request.json['author']
    title = request.json['title']
    genre = request.json['genre']
    pages = request.json['pages']
    isbn = request.json['isbn']
    publisher = request.json['publisher']
    year = request.json['year']
    user_token = current_user_token.token

    print (f"User token: {current_user_token}.")

    book = Book(author, title, genre, pages, isbn, publisher, year, user_token=user_token)

    db.session.add(book)
    db.session.commit()

    response = book_schema.dump(book)

    return jsonify(response)

@api.route('/books/<id>', methods = ['GET'])
@token_required
def get_book(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        book = Book.query.get(id)
        response = book_schema.dump(book)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401

@api.route('/books', methods = ['GET'])
@token_required
def get_books(current_user_token):
    owner = current_user_token.token
    books = Book.query.filter_by(user_token = owner).all()
    response = books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>', methods = ['GET', 'POST'])
@token_required
def update_book(current_user_token, id):
    book = Book.query.get(id)

    book.author = request.json['author']
    book.title = request.json['title']
    book.genre = request.json['genre']
    book.pages = request.json['pages']
    book.isbn = request.json['isbn']
    book.publisher = request.json['publisher']
    book.year = request.gender['year']
    book.user_token = current_user_token.token

    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books/<id>', methods = ['DELETE'])
@token_required
def delete_book(current_user_token, id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)