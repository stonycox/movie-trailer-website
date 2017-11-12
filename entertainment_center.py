# Created By : Tony
# Created On : 11/12/2017
# Description: This file contains list of movies that will be shown on
#              movie trailer website

import media
import fresh_tomatoes


MovieList = []

# Movie No:1 Life is beautiful

life_is_beautiful = media.Movie(
    "Life Is Beautiful",
    "A Jewish Italian book shop owner employs his fertile imagination"
    "to shield his son from the horrors of Nazi camp",
    "http://www.impawards.com/1998/posters/life_is_beautiful_ver1.jpg",
    "https://www.youtube.com/watch?v=pAYEQP8gx3w")

# Movie No:2 Troy

troy = media.Movie(
    "Troy",
    "Troy is a 2004 epic period war film. It is loosely"
    "based on Home's Illiad.",
    "http://www.impawards.com/2004/posters/troy.jpg",
    "https://www.youtube.com/watch?v=znTLzRJimeY")

# Movie No:3 Matrix

matrix = media.Movie(
    "Matrix",
    "The matrix is 1999 science fiction action film",
    "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
    "https://www.youtube.com/watch?v=Q8g9zL-JL8E")

# Movie No:4 Brave Heart

brave_heart = media.Movie(
    "Brave Heart",
    "Brave heart is a 1995 epic war film",
    "http://www.impawards.com/1995/posters/braveheart.jpg",
    "https://www.youtube.com/watch?v=wj0I8xVTV18")

# Movie No:5 500 days of summer

summer = media.Movie(
    "500 Days of Summer",
    "500 days of summer is a 2009 romantic-comedy drama film",
    "http://www.impawards.com/2009/posters/five_hundred_days_of_summer.jpg",
    "https://www.youtube.com/watch?v=BFfsESRNSL8")

# movie No:6  Soul Surfer

soul_surfer = media.Movie(
    "Soul Surfer",
    "Soul Surfer: A True Story of Faith, Family, and Fighting"
    "to Get Back on the Board",
    "http://www.impawards.com/2011/posters/soul_surfer.jpg",
    "https://www.youtube.com/watch?v=_KlpD6dr7Qw")


# Add movies to movie list
MovieList.append(life_is_beautiful)
MovieList.append(troy)
MovieList.append(matrix)
MovieList.append(brave_heart)
MovieList.append(summer)
MovieList.append(soul_surfer)

# Pass movie list to open movies page () method to render Movie trailer website
fresh_tomatoes.open_movies_page(MovieList)
