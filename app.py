from flask import Flask, render_template

app = Flask(__name__)

GRAMMAR_TOPICS = {
    "A1": [
        "Alphabet",
        "Greetings",
        "Articles",
        "Nouns",
        "Present Tense",
        "Personal Pronouns",
        "Question Words"
    ],
    "A2": [],
    "B1": [],
    "B2": [],
    "C1": [],
    "C2": []
}

LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/grammar")
def grammar():
    return render_template("grammar.html")

@app.route("/grammar/topics/<level>")
def grammar_topics(level):

    level = level.upper()

    if level not in LEVELS:
        return "Unknown CEFR level", 404

    return render_template(
        "grammar_topics.html",
        levels=LEVELS,
        selected_level=level,
        topics=GRAMMAR_TOPICS[level]
    )



if __name__ == "__main__":
    app.run(debug=True)

