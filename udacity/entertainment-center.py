import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Extraterrestial Pocahontas story",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                             "kids go to some school or rock?",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                             "about some mouse and chesse",
                             "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                            "www.youtube.com/watch?v=uVeNEbh3A4U")
    
    
midnight_in_paris = media.Movie("Midnight in Paris",
                             "no clue",
                             "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
                             "have to fight for their lives in a war game",
                             "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "www.youtube.com/watch?v=4S9a5V9ODuY")
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
