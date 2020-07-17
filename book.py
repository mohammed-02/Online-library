import web
import lab
The_Power_of_Habit = lab.Library("The Power of Habit",

                                    "Charles Duhigg",

                                    "28 février 2012",

                                    "Lisa souffrait de boulimie, d’alcoolisme, de tabagisme et de surendettement. Un jour,tout a changé : en modifiant une pièce du puzzle de son existence,elle est sortie du cercle vicieux de ses habitudes toxiques",

                                    "https://images-na.ssl-images-amazon.com/images/I/819ZixpQzUL.jpg",

                                    "https://youtu.be/yTSVLMLgY5U")

The_Art_of_Thinking_Clearly= lab.Library("The Art of Thinking Clearly",

                       "Rolf Dobelli",

                       "2013",

                       "Traduit de l'anglais-L'Art de penser clairement est un livre de 2013"
                       " de l'écrivain suisse Rolf Dobelli qui décrit dans de courts chapitres"
                       " 99 les erreurs de pensée les plus courantes - allant des biais cognitifs"
                       " à l'envie et aux distorsions sociales.",

                       "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTnLJljq7d3ICSfKOLqfRhYS-d86p1DRvbVATH8ynNdnXAmKNhq",

                       "https://youtu.be/C2NOTu_fxl8")

Thinking_Fast_and_Slow = lab.Library("Thinking, Fast and Slow",

                              " Daniel Kahneman",

                              "25 octobre 2011",

                              "Système 1 / Système 2 : Les deux vitesses de la pensée est un livre publié en 2011 par le lauréat du prix Nobel d'économie Daniel Kahneman, qui résume les recherches qu'il a effectuées au fil des décennies, souvent en collaboration avec Amos Tversky.",

                              "https://images-na.ssl-images-amazon.com/images/I/41wI53OEpCL._SX332_BO1,204,203,200_.jpg",

                              "https://youtu.be/IRy4t2X_33c")

the_magic_of_thinking_big = lab.Library("the magic of thinking big",

                            "David J. Schwartz",

                            "1959",

                            "L'art du succès et de la réussite en utilisant les capacités"
                            " à l'intérieur de soi.Des dizaines de techniques, de principes,"
                            " d'idées pratiques pleines de bon sens, qui vous rendront capable de maîtriser",

                            "https://images-na.ssl-images-amazon.com/images/I/71LOTNfMchL.jpg",

                            "https://youtu.be/XoGFhCNuDfE")

talk_like_ted = lab.Library("Talk Like TED",

                         " Carmine Gallo",

                         "4 mars 2014",

                         "Les 9 secrets des meilleurs orateurs du monde Les idées sont la monnaie"
                         " du XXIe siècle. Pour réussir, vous devez être capable de vendre vos "
                         "idées de manière convaincante. Cette capacité est LA compétence qui "
                         "vous aidera à réaliser vos rêves",

                         "https://m.media-amazon.com/images/I/41bty9PnFfL.jpg",

                         "https://youtu.be/54vid9p0jRs")

rich_dad_poor_dad = lab.Library("rich dad poor dad",

                                       " Robert Kiyosaki, Lechter, Sharon L",

                                       "1997",

                                       "Père riche, père pauvre est un livre de Robert Kiyosaki et de Sharon"
                                       " Lechter paru en 1997. De style autobiographique, Robert Kiyosaki "
                                       "utilise un ensemble de paraboles et d'exemples tirés de son propre"
                                       " parcours afin de souligner l'importance de développer son intelligence "
                                       "financière.",

                                       "https://m.media-amazon.com/images/I/51bX4hDuBIL.jpg",

                                       "https://youtu.be/Pp7WECKyGYw")

Drive = lab.Library("Drive",

                                         " Daniel H. Pink",

                                         "2018",
                                        "The New York Times bestseller that gives readers a paradigm-shattering "
                                        "new way to think about motivation from the author of When: "
                                        "The Scientific Secrets of Perfect Timing.",

                                        "https://m.media-amazon.com/images/I/41mzE0eBCBL.jpg",

                                         "https://youtu.be/Xj6789sTvPo")

The_Subtle_Art_of_Not_Giving_a_Fck = lab.Library("The Subtle Art of Not Giving a F*ck",

                          "Mark Manson",

                          "13 septembre 2016",

                          "L'Art subtil de s'en foutre : Un guide à contre-courant pour être"
                           " soi-même est le deuxième livre du blogueur et écrivain américain"
                           " Mark Manson.",

                          "https://images-na.ssl-images-amazon.com/images/I/71QKQ9mwV7L.jpg",

                          "https://youtu.be/Ut5NJr4eoHU")

the_art_of_war = lab.Library("the art of war",

                                "Sun Tzu",

                                "2014",

                                "L’Art de la guerre est un court traité de stratégie militaire chinois,"
                                " datant de la période des Printemps et Automnes",

                                "https://kbimages1-a.akamaihd.net/d87c7a64-273f-4680-b690-367e80c33956/1200/1200/False/the-art-of-war-349.jpg",

                                "https://youtu.be/6cBl2fF6LmI")

books = [The_Power_of_Habit, The_Art_of_Thinking_Clearly, Thinking_Fast_and_Slow
    , the_magic_of_thinking_big, talk_like_ted, rich_dad_poor_dad
    , Drive, The_Subtle_Art_of_Not_Giving_a_Fck, the_art_of_war]

web.open_books_page(books)
