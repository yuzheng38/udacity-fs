#!/usr/bin/python
import webbrowser


class Movie(object):
    """ This is my custom Movie class.

    Attributes:
        title: A string representing the title of the movie.
        storyline: A string representing the storyline of the movie.
        poster_image: A URL linking to an online image of the movie poster.
        trailer: A URL linking to a Youtube video of the movie.
    """

    def __init__(self, title, storyline, poster_image, trailer):
        """Inits the Movie class with passed in arguments."""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """Opens the movie trailer/preview in a default web browser."""
        webbrowser.open(self.trailer_youtube_url)
