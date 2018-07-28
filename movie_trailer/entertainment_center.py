#!/usr/bin/python

import fresh_tomatoes
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


surface = Movie("Surface",
               "Surface by Aero Chord",
               ("https://i.ytimg.com/vi/BrCKvKXvN2c/hqdefault.jpg?"
               "sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIJCGAFwAQ==&"
               "rs=AOn4CLC452FeRgiEzd3yROTXGDzIPKLEfQ"),
               "https://www.youtube.com/watch?v=BrCKvKXvN2c")

guitar_sounds = Movie("Guitar Sounds",
                        "Guitar Sounds by Ronald Jenkees",
                        ("https://i.ytimg.com/vi/oLybNuk_Lpo/hqdefault.jpg?"
                        "sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIJCGAFwAQ==&"
                        "rs=AOn4CLBw0N7y8XXQhpLWw8mEvRQc-kkNJA"),
                        "https://www.youtube.com/watch?v=oLybNuk_Lpo")

two_steps = Movie("Two Steps from Hell",
                    "Two Steps from Hell by Victory",
                    ("https://i.ytimg.com/vi/hKRUPYrAQoE/hqdefault.jpg?"
                    "sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIJCGAFwAQ==&"
                    "rs=AOn4CLDF7m2kNocfRRCsbE7Fz6LjiVuKUg"),
                    "https://www.youtube.com/watch?v=hKRUPYrAQoE")

superhero = Movie("Superhero",
                    "Superhero by Unknown Brain",
                    ("https://i.ytimg.com/vi/LHvYrn3FAgI/hqdefault.jpg?"
                    "sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIJCGAFwAQ==&"
                    "rs=AOn4CLBZ2FXirDV74Yp-z_yd6wfC2y9QjA"),
                    "https://www.youtube.com/watch?v=LHvYrn3FAgI")

shape_of_you_flute = Movie("Shape of You Flute",
                           "Shape of you remix in Chinese Flute",
                           ("https://i.ytimg.com/vi/GWZLH7lx6NM/hqdefault.jpg?"
                           "sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIJCGAFwAQ==&"
                           "rs=AOn4CLC8zXe39MfMUSudlaS69qTf92b47Q"),
                           "https://www.youtube.com/watch?v=GWZLH7lx6NM")

monody = Movie("Monody",
               "Monody by TheFatRat",
               ("https://i.ytimg.com/vi/B7xai5u_tnk/hqdefault.jpg?"
               "sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIJCGAFwAQ==&"
               "rs=AOn4CLApna9G7ns2XgYoi7Lzlvnwy3kY-A"),
               "https://www.youtube.com/watch?v=B7xai5u_tnk")


my_movies = [surface,
             guitar_sounds,
             two_steps,
             superhero,
             shape_of_you_flute,
             monody]

fresh_tomatoes.open_movies_page(my_movies)
