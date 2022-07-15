from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def list():
    return render_template("list.html")


@app.route("/question")
def question():
    return render_template("question.html")


@app.route("/question_form")
def question_form():
    return render_template("question_form.html")


if __name__ == "__main__":
    app.run()
