"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """ Starts game if user says yes, otherwise no """

    choice = request.args.get("choice")

    if choice == "yes":
        return render_template("game.html")
    else:
        # return to the goodbye template
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    madlib_files = ["madlib.html", "madlib2.html", "madlib3.html"]
    player_name = request.args.get("name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adj = request.args.get("adj")
    location = request.args.getlist("location")

    #The argument 'madlib.html' is the html form that renders the values.
    #var name (orange) are variables from templates; its value comes from the
    #variables defined inside the View.
    return render_template(choice(madlib_files), person=player_name, color=color,
                            noun=noun, adj=adj, location=location)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
