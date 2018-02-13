
# Video class declartion


class Video():
    """class to keep video information
    """

    def __init__(self, video_title, video_url):
        """Attributes:
             attr1(str): Video title
             attr2(str): Video URL
        """
        self.title = video_title
        self.trailer_youtube_url = video_url

# Movies class declartion inherits from Video


class Movie(Video):
    """class to keep movie information
    """

    def __init__(self, video_title, video_url, movie_storyline, poster_image):
        """Attributes:
             attr1(str): Video title
             attr2(str): Video URL
             attr3(str): Movie storyline
             attr4(str): Poster image URL
        """
        Video.__init__(self, video_title, video_url,)
        self.poster_image_url = poster_image
