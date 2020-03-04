from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome Home!"
@app.route("/<text>")
def displayTest(text):
    return text
@app.route("/splitter/<text>")
def splitter(text):
    return render_template("splitter.html", string=text)

if __name__ == "__main__":
    app.run(port=8080)
