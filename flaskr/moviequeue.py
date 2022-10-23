from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('moviequeue', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    if request.method == 'POST':
        #Switch over to JS after upvote features inplace
        add_movie = request.form['input']
        add_movie = add_movie.replace('[', '').replace(']','')
        add_movies = add_movie.split(',')

        db.execute('INSERT OR IGNORE INTO queue (movie_id, title, votes)'
            ' VALUES (?, ?, ?)', (int(add_movies[0]), add_movies[1], int(add_movies[2])),
            )
        db.commit()

    movies = db.execute(
        'SELECT movie_id, title, votes'
        ' FROM queue'
        ' ORDER BY votes DESC, title'
    ).fetchall()
    return render_template('index.html', movies=movies)

@bp.route('/search', methods=('GET', 'POST'))
@login_required
def search():
    if request.method == 'POST':
        print('POST ENDPOINT ERROR')
        db.execute(
            'INSERT INTO movie (movie_id, votes, title)'
            ' VALUES (%s,%s, %s)', ('''movie_id, votes, title''')
            )
        db.commit()
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