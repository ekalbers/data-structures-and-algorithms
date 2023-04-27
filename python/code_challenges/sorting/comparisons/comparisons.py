import re
# from code_challenges.sorting.comparisons.movies import movies


class Movie:
    def __init__(self, title='None', year=0, genres=[]):
        self.title = title
        self.year = year
        self.genres = genres


def comparisons(lst, sort_attr='title'):
    n = len(lst)

    if n > 1:
        mid = int(n / 2)
        left = lst[0:mid]
        right = lst[mid:len(lst)]
        comparisons(left, sort_attr)
        comparisons(right, sort_attr)
        if sort_attr == 'title':
            merge(left, right, lst, sort_title)
        elif sort_attr == 'year':
            merge(left, right, lst, sort_year)
        else:
            print('invalid sort attribute')


def merge(left, right, lst, srt):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if srt(left[i], right[j]) == 1:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        for x in range(j, len(right)):
            lst[k] = right[j]
            k += 1
            j += 1
    else:
        for x in range(i, len(left)):
            lst[k] = left[i]
            k += 1
            i += 1


def sort_title(left, right):
    pattern = r'^(A|a|An|an|The|the)\s(.*)'
    left = left.title
    right = right.title
    match = re.match(pattern, left)
    if match:
        left = match.group(2)
    match = re.match(pattern, right)
    if match:
        right = match.group(2)
    if left < right:
        return 1
    elif left > right:
        return -1
    return 0


def sort_year(left, right):
    if left.year > right.year:
        return 1
    return 0


if __name__ == '__main__':
    pass
    # movies1 = movies
    # for i, movie in enumerate(movies1):
    #     movies1[i] = Movie(movie['title'], movie['year'], movie['genres'])
    #
    # comparisons(movies1, 'title')
    # for movie in movies1:
    #     print(movie.title)


