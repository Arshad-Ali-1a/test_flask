from flask import Flask
from users_blueprint import users_bp

app = Flask(__name__)

# Register blueprints.
app.register_blueprint(users_bp, url_prefix='/users')

@app.route('/')
def home():
    return "Welcome to the Online Book Store!"

if __name__ == '__main__':
    app.run(debug=True)
