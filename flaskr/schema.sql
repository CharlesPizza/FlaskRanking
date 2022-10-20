DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS all_movies;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE movie (
  movie_id INTEGER PRIMARY KEY,
  votes INTEGER NOT NULL,
  title TEXT NOT NULL
);

CREATE TABLE all_movies (
  movie_id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  votes INTEGER NOT NULL,
  rating INTEGER NOT NULL
);