from media import Movie
from fresh_tomatoes import open_movies_page

# Movies variables declarations


blade_runner_2049 = Movie("Blade Runner 2049",
                          "https://www.youtube.com/watch?v=dZOaI_Fn5o4",
                          "Thirty years after the events of the first film, a "
                          "new blade runner",
                          "http://br.web.img3.acsta.net/pictures/17/08/25/11/5"
                          "8/463146.jpg")

star_trek = Movie("Star Trek",
                  "https://www.youtube.com/watch?v=3PM1pvOzn_w",
                  "In 2233, over 30 years before The Original Series wa"
                  "s supposed to take places",
                  "https://resizing.flixster.com/ovxhoYYmiNj32jZ5M41Tno"
                  "PdbfE=/206x305/v1.bTsxMTE3Mzg0MztqOzE3Njc5OzEyMDA7OD"
                  "AwOzEyMDA")

avengers = Movie("Avengers",
                 "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                 "A group of awesome heroes",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9"
                 "/TheAvengers2012Poster.jpg/220px-TheAvengers2012Post"
                 "er.jpg")

# Movies list created


movies_list = [blade_runner_2049, star_trek, avengers]

# Generate the website


open_movies_page(movies_list)
