from flask import Flask, Response
import random


app = Flask(__name__)


def construct_compliment():
    compliment = ""

    with open("adjectives.txt") as f:
        adjectives = f.readlines()
        adjectives = [x.strip() for x in adjectives]

        compliment = ", ".join(random.sample(adjectives, 2))

    with open("nouns.txt") as f:
        nouns = f.readlines()
        nouns = [x.strip() for x in nouns]
        
        compliment = compliment + " " + random.sample(nouns, 1)[0]
    
    print(compliment)
    
    return compliment



@app.route("/sms", methods=["GET", "POST"])
def sms():
    compliment = construct_compliment()
    print(compliment)

    resp = """
    <Response>
        <Message>
            Happy Galentines Day, you {}
        </Message>
    </Response>""".format(compliment)

    return Response(resp, mimetype="text/xml")


if __name__ == '__main__':
    app.run(debug=True)
