# Created By : Tony
# Created On : 11/12/2017
# Description: This file contains Movie class that defines properties and
#              functions required for Movie trailer website


class Movie():
    """This movie class defines structure of data that we are going
    to store for each movie"""

    def __init__(self, title, story_line, poster_image_url,
                 trailer_youtube_url):
        """This is the constructor method of movie class.
        It initializes the movie class properties when invoked"""
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
