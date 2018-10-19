# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

matrix = media.Movie('The Matrix',
        'Cool movie',
        'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
        'https://www.youtube.com/watch?v=m8e-FF8MsqU');

lordofring = media.Movie('The lord of Ring',
                         'The magic world',
                         'https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg',
                         'https://www.youtube.com/watch?v=rCZ3SN65kIs');

Guardians_of_the_Galaxy = media.Movie('Guardians of the Galaxy ', 'The cosmic world',
                                      'https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg',
                                      'https://www.youtube.com/watch?v=d96cjJhvlMA'); 

movies = [matrix, lordofring, Guardians_of_the_Galaxy];
fresh_tomatoes.open_movies_page(movies);
