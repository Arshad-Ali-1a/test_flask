from flask import Blueprint, jsonify, request

books_bp = Blueprint('books', __name__)

# Sample book inventory (would typically be a database in a real application)
book_inventory = [
    {"id": 1, "title": "Python Basics", "author": "John Smith", "price": 29.99, "stock": 10},
    {"id": 2, "title": "Web Development with Flask", "author": "Jane Doe", "price": 34.99, "stock": 5},
    {"id": 3, "title": "Data Science Handbook", "author": "Alex Johnson", "price": 44.99, "stock": 7}
]

@books_bp.route('/')
def list_books():
    return jsonify(book_inventory)

@books_bp.route('/<int:book_id>')
def get_book(book_id):
    book = next((book for book in book_inventory if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@books_bp.route('/add', methods=['POST'])
def add_book():
    new_book = request.json
    new_book['id'] = len(book_inventory) + 1
    book_inventory.append(new_book)
    return jsonify(new_book), 201