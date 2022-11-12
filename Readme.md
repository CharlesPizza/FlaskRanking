## Movie Queue Ranking
This Project is a simple movie queue system built for voting on movies to watch
in discord. The project features 
* Flask API interaction
* HTMX requests
* SQLite3 database
    * Database of horror movies
    * Users
    * Queued Movies and User Votes
* boilerplate login features.

## /Index/
The index displays the movies currently queued. Logged in users can vote to add
their vote, or vote a second time to remove it.
![Alt text](Images/Flask%20Movie%20Queue%20Page.png "Title")


## /search
This page features an HTMX search bar. The HTMX updates the returned results at 
the designated rate of 250ms after keyup. Results are displayed in a table format
with a button to submit the movie to the MovieQueue table, then making it available
for voting on /index

