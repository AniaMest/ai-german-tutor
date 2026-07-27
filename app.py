from flask import Flask, render_template

app = Flask(__name__)

GRAMMAR_TOPICS = {
    "A1": [
        {
            "id": "der-satz",
            "title": "Der Satz"
        },
        {
            "id": "die-satzfrage",
            "title": "Die Satzfrage"
        },
        {
            "id": "w-fragen",
            "title": "W-Fragen"
        },
        {
            "id": "die-satzklammer",
            "title": "Die Satzklammer"
        },
        {
            "id": "zeitangaben-im-satz",
            "title": "Zeitangaben im Satz"
        },
        {
            "id": "ortsangaben-hier-dort-da",
            "title": "Ortsangaben im Satz: <em>hier</em>, <em>dort</em>/<em>da</em>"
        },
        {
            "id": "es-im-satz",
            "title": "<em>es</em> im Satz"
        },
        {
            "id": "adjektive-im-satz",
            "title": "Adjektive im Satz"
        },
        {
            "id": "saetze-verbinden",
            "title": "Sätze verbinden (multiple)"
        },
        {
            "id": "verneinung-im-satz",
            "title": "Verneinung im Satz"
        },
        {
            "id": "zuerst-dann-danach-zum-schluss",
            "title": "<em>Zuerst</em>, <em>dann</em>, <em>danach</em>, <em>zum Schluss</em> im Satz"
        },
        {
            "id": "nomen-und-artikel",
            "title": "Nomen und Artikel (multiple)"
        },
        {
            "id": "plural",
            "title": "Nomen im Plural"
        },
        {
            "id": "praepositionen",
            "title": "Präpositionen (multiple)"
        },
        {
            "id": "pronomen-man",
            "title": "Pronomen <em>man</em>"
        },
        {
            "id": "wie-oft",
            "title": "Wie oft? <em>immer</em>, <em>meistens</em>, <em>oft</em>, <em>manchmal</em>, <em>nie</em>"
        },
        {
            "id": "verben",
            "title": "Verben (multiple)"
        },
        {
            "id": "komposita",
            "title": "Komposita"
        },
        {
            "id": "possessivartikel-nominativ-akkusativ",
            "title": "Possessivartikel: Nominativ und Akkusativ"
        },
        {
            "id": "fragewort-welch",
            "title": "Fragewort <em>welch-</em> (multiple)"
        },
        {
            "id": "personalpronomen",
            "title": "Personalpronomen"
        },
        {
            "id": "praepositionen-in-an-nach-auf",
            "title": "Präpositionen: <em>in</em>, <em>an</em>, <em>nach</em>, <em>auf</em> + Akkusativ"
        },
        {
            "id": "adjektive-vor-dem-nomen",
            "title": "Adjektive vor dem Nomen: unbestimmter Artikel im Akkusativ"
        },
        {
            "id": "graduierung",
            "title": "Graduierung"
        },
        {
            "id": "komparativ",
            "title": "Vergleiche: der Komparativ"
        },
        {
            "id": "imperativ",
            "title": "Imperativ"
        },
        {
            "id": "modalverben",
            "title": "Modalverben: <em>können</em>, <em>möchten</em>, <em>mögen</em>, <em>wollen</em>, <em>sollen</em>, <em>müssen</em>"
        },
        {
            "id": "perfekt",
            "title": "Perfekt: regelmäßige und unregelmäßige Verben (multiple)"
        }
    ],
    "A2": [],
    "B1": [],
    "B2": [
        {
            "id": "weil-da-deshalb-deswegen",
            "title": "<em>weil</em>, <em>da</em>, <em>deshalb</em>, <em>deswegen</em>"
        }
    ],
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

@app.route("/grammar/topics/<level>/<topic_id>")
def topic_page(level, topic_id):

    topic = next(
        (t for t in GRAMMAR_TOPICS[level] if t["id"] == topic_id),
        None
    )

    return render_template(
        "topic.html",
        level=level,
        topic=topic
    )

@app.route("/grammar/topics/<level>/<topic_id>/exercise")
def exercise_page(level, topic_id):

    import json

    path = f"data/exercises/grammar/{level.lower()}/{topic_id}.json"

    with open(path, encoding="utf-8") as f:
        exercise = json.load(f)
    return render_template(
        "exercise.html",
        exercise=exercise,
        level=level,
        topic_id=topic_id
    )

if __name__ == "__main__":
    app.run(debug=True)

