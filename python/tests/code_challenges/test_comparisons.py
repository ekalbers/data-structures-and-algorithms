from code_challenges.sorting.comparisons.comparisons import Movie, comparisons


movies = [
  {
    'title': "Beetlejuice",
    'year': 1988,
    'genres': ["Comedy", "Fantasy"]
  },
  {
    'title': "The Cotton Club",
    'year': 1984,
    'genres': ["Crime", "Drama", "Music"]
  },
  {
    'title': "The Shawshank Redemption",
    'year': 1994,
    'genres': ["Crime", "Drama"]
  },
  {
    'title': "Crocodile Dundee",
    'year': 1986,
    'genres': ["Adventure", "Comedy"]
  },
  {
    'title': "Valkyrie",
    'year': 2008,
    'genres': ["Drama", "History", "Thriller"]
  },
  {
    'title': "Ratatouille",
    'year': 2007,
    'genres': ["Animation", "Comedy", "Family"]
  },
  {
    'title': "City of God",
    'year': 2002,
    'genres': ["Crime", "Drama"]
  },
  {
    'title': "Memento",
    'year': 2000,
    'genres': ["Mystery", "Thriller"]
  },
  {
    'title': "The Intouchables",
    'year': 2011,
    'genres': ["Biography", "Comedy", "Drama"]
  },
  {
    'title': "Stardust",
    'year': 2007,
    'genres': ["Adventure", "Family", "Fantasy"]
  },
]

expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# Expected test output of test #2
expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];


def test_comparisons_year():
    test_movies = []
    for movie in movies:
        test_movies.append(Movie(movie['title'], movie['year'], movie['genres']))
    comparisons(test_movies, 'year')
    actual = []
    for movie in test_movies:
        actual.append(movie.title)
    assert actual == expected1


def test_comparisons_title():
    test_movies = []
    for movie in movies:
        test_movies.append(Movie(movie['title'], movie['year'], movie['genres']))
    comparisons(test_movies, 'title')
    actual = []
    for movie in test_movies:
        actual.append(movie.title)
    assert actual == expected2


def test_comparisons_empty_list():
    actual = []
    comparisons(actual)
    expected = []
    assert actual == expected
