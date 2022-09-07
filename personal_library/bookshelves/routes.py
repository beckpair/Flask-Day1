from flask import Blueprint, render_template

shelves = Blueprint('shelves', __name__, template_folder= 'shelves_templates')

@shelves.route('/bookshelves')
def bookshelves():
    return render_template('shelves.html')