from flask import Flask, request

app = Flask(__name__)


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    movies = {
        "favourite": ["A New Hope", "Empire Strikes Back", "Return Of The Jedi",
                      "The Force Awakens", "Jaws", "Predator", "Mad Max",
                      "Back to the Future", "2001: A Space Odyssey", "Robocop",
                      "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                      "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

        "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
                  "Alien Resurrection", "Twilight"]

    }
    if request.method == "GET":
        content = """
            <form action="/movies" method = "POST">
                <label>
                    Insert Title:<br>
                    <input type="text"
                            name = "movie">
                </label>
                <label>
                    <button type="submit">
                    Submit
                    </button>
                </label>
                
            </form>
            """
        return content
    else:
        movie = request.form['movie']
        if movie.title() in movies['favourite']:
            return f"Favourite"
        elif movie.title() in movies['hated']:
            return f"Hated"
        else:
            return f"No such a movie! "


if __name__ == "__main__":
    app.run(debug=True)
