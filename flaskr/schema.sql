DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS all_movies;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE queue (
  movie_id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
);

CREATE TABLE votes (
  movie_id int NOT NULL,
  user_id int,
  FOREIGN KEY (movie_id) REFERENCES queue(movie_id),
  FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE all_movies (
  movie_id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  votes INTEGER NOT NULL,
  rating INTEGER NOT NULL
);