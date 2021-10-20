"""
author: Patrick Williamson
Date: October 20th 2020
Computing id: upm8pb
"""


def get_name(movie):
    """
    :param movie: given the movie list
    :return: return the first variable of the list which is the name
    """
    name = movie[0]
    return name


def get_gross(movie):
    """
    :param movie: given the movie list
    :return: return the second variable of the list which is the total gross of the movie
    """
    gross = movie[1]
    return gross


def get_rating(movie):
    """
    :param movie: given the movie list
    :return: return the third variable of the list which is the rating of the movie
    """
    rating = movie[3]
    return rating


def get_num_ratings(movie):
    """
    :param movie: given the movie list
    :return: return the fourth variable of the list which is the number of ratings for the movie
    """
    num_ratings = movie[4]
    return num_ratings


def better_movies(movie_name, movies_list):
    """

    :param movie_name: the name of the movie we want to compare with the entire list of moves
    :param movies_list: the list of all the movies and their stats
    :return: a list of all movies that have a higher rating than the rating of the movie we inputed
    """

    # set up the function with some variables
    count = 0
    i = 0
    results = []

    # we need to find the name of var movie_name in the list
    for i in range(0, len(movies_list)):
        count = movies_list[i].count(movie_name)
        i += 1
        if count == 1:
            movie = movies_list[i - 1]

    # now we need to compare the rating of our movie with all the movies in the list
    for i in range(0, len(movies_list)):
        if get_rating(movie) < get_rating(movies_list[i - 1]):
            results.append(movies_list[i - 1])

    return results


def average(category, movies_list):
    """
    :param category: given one of the 3 options
    :param movies_list: the list of movies and their stats
    :return: the average of the option
    """

    answer = 0

    #vif loops that take the input of the variables we can calculate
    if category == 'rating':

        # now we add together the rating variable for each movie

        for i in range(0, len(movies_list)):
            answer += get_rating(movies_list[i])

    elif category == 'gross':
        for i in range(0, len(movies_list)):
            answer += get_gross(movies_list[i])

    elif category == 'number of ratings':
        for i in range(0, len(movies_list)):
            answer += get_num_ratings(movies_list[i])

    # return the answer but we need to make sure we divide by the amount of variables counted
    return answer / (len(movies_list))
