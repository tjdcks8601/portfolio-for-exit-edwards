import requests

def SearchMovies(query, year) :
    params = {
        "api_key" : "bd8a0564139e17aeaec0a040e09be1be",
        "language" : "ko",
        "page" : "1",
        "query" : query,
        "include_adult" : "true",
        "year" : year
    }

    url = "https://api.themoviedb.org/3/search/movie"