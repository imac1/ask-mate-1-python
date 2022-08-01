from flask import Flask, render_template, request, redirect, url_for
import data_manager


app = Flask(__name__)


@app.route("/")
def list():
    questions_header = data_manager.get_questions_header()
    questions_list = data_manager.display_qs()
    return render_template(
        "list.html", questions_header=questions_header, questions_list=questions_list
    )


@app.route("/question")
def question():
    return render_template("question.html")


@app.route("/question_form")
def question_form():
    return render_template("question_form.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
