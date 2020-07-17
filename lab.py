class Video():

    def __init__(self, title,Writer , year):
        self.title = title
        self.Writer = Writer
        self.year = year


class Library(Video):

    def __init__(self, book_name, book_Writer, book_year
                 , book_story_line, book_poster_url
                 , book_trialer_url):

        Video.__init__(self, book_name, book_Writer, book_year)

        self.storyline = book_story_line
        self.poster_image_url = book_poster_url
        self.trailer_youtube_url = book_trialer_url