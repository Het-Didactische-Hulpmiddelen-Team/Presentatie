from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome Home!"

@app.route("/<text>")
def displayTest(text):
    return text

if __name__ == "__main__":
    app.run(port=8080)
