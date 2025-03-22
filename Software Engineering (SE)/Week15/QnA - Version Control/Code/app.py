from flask import Flask, render_template

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.htm")

@app.route("/")
def hello_world():
    return render_template('index.html', message="Intro to Git")

if __name__ == "__main__":
    app.run(debug=True)