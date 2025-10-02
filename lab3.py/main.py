
from movies_data import movies
from movies_utils import (
    is_above_55,
    filter_above_55,
    movies_by_category,
    average_imdb,
    average_category_imdb
)

print(is_above_55(movies[0]))
print("Movies above 5.5:", filter_above_55(movies))
print("Romance movies:", movies_by_category(movies, "Romance"))
print("Average IMDB of all movies:", average_imdb(movies))
print("Average IMDB of Suspense:", average_category_imdb(movies, "Suspense"))
