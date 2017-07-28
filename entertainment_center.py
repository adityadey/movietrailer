import fresh_tomatoes
import media

# Creating instances of class media to pass on parameters to Movie
wonder_woman = media.Movie("Wonder Woman",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

logan = media.Movie("Logan",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

dunkirk = media.Movie("Dunkirk",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

john_wick_2 = media.Movie("John Wick Chapter 2",
                          "https://upload.wikimedia.org/wikipedia/en/3/31/John_Wick_Chapter_Two.png",
                          "https://www.youtube.com/watch?v=LZrX9mffH8Y")

baby_driver = media.Movie("Baby Driver",
                          "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",
                          "https://www.youtube.com/watch?v=z2z857RSfhk")

the_lego_batman = media.Movie("The Lego Batman",
                              "https://upload.wikimedia.org/wikipedia/en/6/61/The_Lego_Batman_Movie_PromotionalPoster.jpg",
                              "https://www.youtube.com/watch?v=rGQUKzSDhrg")

# Creating a list of movies
movies = [wonder_woman, logan, dunkirk, john_wick_2, baby_driver, the_lego_batman]
# The movie page in html is opened with the list being passed on to open_movies_page function
fresh_tomatoes.open_movies_page(movies)
