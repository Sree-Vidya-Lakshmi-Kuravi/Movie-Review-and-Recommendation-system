from utils import *

path = r'MRS_without_SQL\data\movies.csv'
def view_all_movies():
    movie_data = read_csv(path)

    # Handling empty data
    if not movie_data:
        print("No movies found")

    print(f"{'Movie ID':<10} {'Movie Title':<50} {'Movie Genre':<20} {'Release Year':<15}")
    print("-" * 90)
    for m in movie_data:
        print(f"{m['id']:<10} {m['title']:<50} {m['genre']:<20} {m['release_year']:<15}")


def add_movie(movie_title, movie_genre, movie_release_year):
    movies = read_csv(path)
    new_movie = {
        'id': generate_id(path),
        'title': movie_title,
        'genre': movie_genre,
        'release_year': movie_release_year
    }
    write_row(path, new_movie)


def get_movie_by_id(movie_id: str):
    movies = read_csv(path)
    for m in movies:
        if m['id'] == movie_id:
            return m
    return "Movie not found"

# print(get_movie_by_id('3'))

def generate_movie_id(movie_title: str):
    movies = read_csv(path)
    for m in movies:
        if m['title'].lower().strip() == movie_title.lower().strip():
            return m['id']
    return "Movie not found"

print(generate_movie_id('godavari'))