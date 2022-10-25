from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
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

        db.execute('INSERT OR IGNORE INTO queue (movie_id, title)'
            ' VALUES (?, ?)', (int(add_movies[0]), add_movies[1]),
            )
        db.execute('INSERT OR IGNORE INTO votes (movie_id)'
            ' VALUES ((SELECT movie_id FROM queue WHERE movie_id = ?))', (int(add_movies[0]),),
            )
        print(int(add_movies[0]))

        db.commit()
    movies = db.execute('SELECT queue.movie_id, queue.title, COUNT(votes.user_id) as count'
        ' FROM votes CROSS JOIN queue ON votes.movie_id = queue.movie_id'
        ' GROUP BY votes.movie_id ORDER BY count DESC;'
        ).fetchall()
    print(type(movies))
    return render_template('index.html', movies=movies)

@bp.route('/vote', methods=('GET','POST'))
@login_required
def vote():
    db = get_db()
    if request.method == 'GET':
        print('OOPS')
    if request.method == 'POST':
        user_id = session['user_id']
        r = db.execute('SELECT * FROM votes WHERE (movie_id, user_id) = (?, ?)', (int(request.form['vote']), int(user_id))).fetchone()
        print(r)
        if r is None:
            db.execute('INSERT INTO votes (movie_id, user_id)'
                ' VALUES (?, ?)', (int(request.form['vote']), int(user_id)))
        else:
            db.execute('DELETE FROM votes WHERE movie_id = ? AND user_id = ?', (int(request.form['vote']), int(user_id)))
        db.commit()

        print(session['user_id'])
        print(request.form['vote'])
    return redirect('/')

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