from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('moviequeue', __name__)
@bp.route('/')
def index():
    db = get_db()
    movies = db.execute(
        'SELECT p.movie_id, votes, title'
        ' FROM movie p'
        ' ORDER BY votes DESC'
    ).fetchall()
    return render_template('index.html', movies=movies)

@bp.route('/search', methods=('GET', 'POST'))
@login_required
def search():
    return render_template('search.html')

@bp.get('/search_movies')
def search_movies():
    movies = []
    db = get_db()
    q = request.args.get('q')
    if q:
        movies = []
        r = db.execute(
            'SELECT * FROM all_movies WHERE title LIKE ?', ('%'.join([q,'%']),)
        ).fetchall()
        for movie in r:
            if q.lower() in movie['title'].lower():
                movies.append(movie)
        # movies = r.json()['movies']
        return render_template('movies.html', movies=movies)
    return ''