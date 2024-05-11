from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/moska/PycharmProjects/pythonProject/instance/books.sqlite'
db = SQLAlchemy(app)

# Define your models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(50))

# Create all database tables inside an application context
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html', image_file='book-shelves.jpg')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form data
        username = request.form['username']
        password = request.form['password']
        # Add your login logic here
        return redirect(url_for('home'))  # Redirect to home after successful login
    return render_template('login.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process the registration form data
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        # Add your registration logic here
        return redirect(url_for('login'))  # Redirect to login after successful registration
    return render_template('register.html')

@app.route('/books')
def books():
    # Fetch all books from the database
    books = Book.query.all()
    return render_template('books.html', books=books)

# Add Manage Books functionality
@app.route('/manage_books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        language = request.form['language']
        new_book = Book(title=title, author=author, language=language)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('manage_books.html')

if __name__ == '__main__':
    app.run(debug=True)
