
#Video class declartion
class Video():
    """class to keep video information

       Attributes:
            attr1(str): Video title
            attr2(str): Video URL
    """
    def __init__(self, video_title, video_url):
        self.title = video_title
        self.trailer_youtube_url = video_url

#Movies class declartion inherits from Video
class Movie(Video):
    """class to keep movie information

       Attributes:
            attr1(str): Video title
            attr2(str): Video URL
            attr3(str): Movie storyline
            attr4(str): Poster image URL
    """
    def __init__(self,video_title, video_url, movie_storyline, poster_image):
        Video.__init__(self, video_title, video_url,)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
