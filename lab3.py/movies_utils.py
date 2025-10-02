
from movies_data import movies

def is_above_55(movie):
    return movie["imdb"] > 5.5

def filter_above_55(movies):
    return [m for m in movies if m["imdb"] > 5.5]

def movies_by_category(movies, category):
    return [m for m in movies if m["category"].lower() == category.lower()]

def average_imdb(movies):
    return sum(m["imdb"] for m in movies) / len(movies)

def average_category_imdb(movies, category):
    category_movies = movies_by_category(movies, category)
    if not category_movies:
        return 0
    return average_imdb(category_movies)
