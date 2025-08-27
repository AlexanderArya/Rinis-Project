from flask import Blueprint, render_template

landingPage = Blueprint("init", __name__)

@landingPage.route("/")
def home():
    # ini akan cari ke ./templates/index.html
    return render_template("index.html")
