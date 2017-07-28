import webbrowser

# Defining the class of Movie
class Movie():

# Defining the constructor in order to initialise the variables    
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Defining show trailer function in order to show movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
