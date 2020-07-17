import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Library Trailer Website</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" lab="screen">

        #story .p{

            font-size: 15px;
            text-align: left;
        }
        .book{

            color: #990000;
            text-decoration: none;
        }
        .book:hover{

            color: #660000;
            font-weight: bold;
        }
        .header{

                background: #333;
                color: #FFF;
                font-size: 30px;
                text-align: center;
                padding: 20px;
        }
        .navigation{

                background: #d9d9d9;
                color: #676767;
                font-size: 20px;
                font-color : #FFFFFF;
                text-align: center;
                padding: 10px;
        }
        .container
        {
            padding: 50px;
        }
        #book-trailer .navbar-brand{
            text-align : center;
            text-color : #FFFFFF
         }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 150%;
        }
        .book-tile {

            color: #FFFFFF;
            margin-bottom: 20px;
            padding-top: 30px;
            padding-bottom: 30px;
        }
        .book-tile p{

            color: #ffe6e6;

        }
        .book-tile p:hover{

            color: #660000;
            font-weight: bold;
            font-size: 15px

        }
        .book-tile:hover {

            color: #660000;
            background-color: #bfbfbf;
            cursor: pointer;
        }
        .scale-lab {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-lab iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.book-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the books when the page loads
        $(document).ready(function () {
          $('.book-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body style="background-color: #191919;">
    <!-- Trailer Video Modal -->

    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://promotions.newegg.com/nepro/15-3345/img/icon_closeButton_256.png" width = "30" hieght = "30" title = "Close" />
          </a>
          <div class="scale-lab" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->

    <div class="header"> Welcome To My First Website Ever</div>
        <div class="navigation">
         <a class = "book" href = "#">  Library Trailer! </a>
        </div>

    <div class="container">
      {book_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 book-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h3>{book_title}</h3>
    <p style="text-align:left;" > Story Line: {book_storyline}</p>
    <p style="text-align:left;" > Duration: {book_Writer}</p>
    <p style="text-align:left;" > Year: {book_year}</p>
</div>

'''


def create_book_tiles_content(books, book_tile_content=None):
    
    # The HTML content for this section of the page
    content = ''
    for book in books:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', book.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', book.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the book with its content filled in
        content += book_tile_content.format(
            book_title=book.title,
            book_duration=book.duration,
            book_year=book.year,
            book_storyline=book.storyline,
            poster_image_url=book.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_books_page(books):
    # Create or overwrite the output file
    output_file = open('web.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(book_tiles=create_book_tiles_content(books))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible