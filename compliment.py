from flask import Flask, Response
import random


def construct_compliment():
    compliment = ""

    with open("adjectives.txt") as f:
        adjectives = f.readlines()
        adjectives = [x.strip() for x in adjectives]

        num_compliments = random.randint(2, 5)
        compliment = ", ".join(random.sample(adjectives, num_compliments))

    with open("nouns.txt") as f:
        nouns = f.readlines()
        nouns = [x.strip() for x in nouns]

        compliment = compliment + " " + random.sample(nouns, 1)[0]

    return compliment


app = Flask(__name__)


@app.route("/sms", methods=["GET", "POST"])
def sms():
    compliment = construct_compliment()

    resp = """
    <Response>
        <Message>
            Happy Galentine's Day, you {}
        </Message>
    </Response>""".format(compliment)

    return Response(resp, mimetype="text/xml")


app.run(debug=True)
