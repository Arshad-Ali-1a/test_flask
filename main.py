from flask import Flask
from books_blueprint import books_bp
from users_blueprint import users_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(users_bp, url_prefix='/users')

@app.route('/')
def home():
    return "Welcome to the Online Book Store!"

if __name__ == '__main__':
    app.run(debug=True)