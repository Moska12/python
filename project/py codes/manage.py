from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Your existing Flask routes...

@app.route('/books', methods=['GET'])
def get_books():
    return render_template('books.html', books=library.display_books())

@app.route('/books', methods=['POST'])
def add_book():
    data = request.form
    title = data.get('title')
    author = data.get('author')
    genre = data.get('genre')
    library.add_book(title, author, genre)
    return redirect('/books')  # Redirect to the books page after adding a book

# Additional routes...

if __name__ == '__main__':
    app.run(debug=True)
