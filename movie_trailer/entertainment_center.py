#!/usr/bin/python
import fresh_tomatoes
import media


black_panther = media.Movie("Black Panther",
                            ("After the death of his father, the king of "
                             "Wakanda, young T'Challa returns home to the "
                             "isolated high-tech African nation to succeed to "
                             "the throne and take his rightful place as king. "
                             "But when a powerful enemy reappears, T'Challa's "
                             "mettle as king - and Black Panther - is tested "
                             "when he's drawn into a formidable conflict that "
                             "puts the fate of Wakanda and the entire world at"
                             " risk."),
                            "https://i.ytimg.com/vi_webp/QoTbGtV9Zpk/movieposter.webp",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU&t=46s")

avengers = media.Movie("Avengers: Infinity War",
                       ("An unprecedented cinematic journey ten years in the "
                        "making and spanning the entire Marvel Cinematic "
                        "Universe, Marvel Studios' Avengers: Infinity War "
                        "brings to the screen the ultimate, deadliest showdown"
                        " of all time. The Avengers and their Super Hero "
                        "allies must be willing to sacrifice all in an attempt"
                        " to defeat the powerful Thanos before his blitz of "
                        "devastation and ruin puts an end to the universe."),
                       "https://i.ytimg.com/vi_webp/OxzKb4a1Qc4/movieposter.webp",
                       "https://www.youtube.com/watch?v=OxzKb4a1Qc4")

bleeding_steel = media.Movie("Bleeding Steel",
                             ("In an action-packed drama reminiscent of '80s "
                              "techno-scifi thrillers, Jackie Chan stars as "
                              "Lin, a police inspector in modern Hong Kong. "
                              "While tracking down a deranged, mecha-enhanced "
                              "villain, Lin discovers that a geneticist's lost"
                              " bio-chemical invention has been surgically "
                              "implanted into his missing daughter. With the "
                              "help of a young hacker, Lin connects the dots "
                              "between the device that haunts his daughter, hi"
                              "s enemy's sinister army, and a strange cultural"
                              " phenomenon called 'Bleeding Steel.'"),
                             "https://i.ytimg.com/vi_webp/klmJ2a-8EYo/movieposter.webp",
                             "https://www.youtube.com/watch?v=klmJ2a-8EYo&list=PLHPTxTxtC0iZ24WpHQ6pLuAHz-R-Oj-uf")

equalizer = media.Movie("The Equalizer",
                        ("McCall, who has put his mysterious past behind him, "
                         "comes out of self-retirement to serve vengeance "
                         "against anyone who would brutalize the helpless."),
                        "https://i.ytimg.com/vi_webp/vTQIRJzKdJo/movieposter.webp",
                        "https://www.youtube.com/watch?v=vTQIRJzKdJo&list=PLHPTxTxtC0ial7mOT-Srrguvokjvlcbg7")

rampage = media.Movie("Rampage",
                      ("Primatologist Davis (Dwayne Johnson) shares an "
                       "unshakable bond with George, the extraordinarily "
                       "intelligent, silverback gorilla who has been in his "
                       "care since birth."),
                      "https://i.ytimg.com/vi_webp/iWekPHIesM0/movieposter.webp",
                      "https://www.youtube.com/watch?v=iWekPHIesM0&t=65s")

jurassic_world = media.Movie("Jurassic World",
                             ("The Jurassic World theme park lets guests "
                              "experience the thrill of witnessing actual "
                              "dinosaurs, but something ferocious lurks behind"
                              " the park's attractions - a genetically modifi"
                              "ed dinosaur with savage capabilities. When the "
                              "massive creature escapes, chaos erupts across "
                              "the island. Now it's up to Owen (Chris Pratt) "
                              "and Claire (Bryce Dallas Howard) to save the "
                              "park's tourists from an all-out prehistoric "
                              "assault."),
                             "https://i.ytimg.com/vi_webp/e6d0VF3TCiQ/movieposter.webp",
                             "https://www.youtube.com/watch?v=e6d0VF3TCiQ")

my_movies = [black_panther,
             avengers,
             bleeding_steel,
             equalizer,
             rampage,
             jurassic_world]

fresh_tomatoes.open_movies_page(my_movies)
