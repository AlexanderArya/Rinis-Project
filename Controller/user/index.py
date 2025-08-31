from flask import Blueprint, render_template
from Model import model_data

landingPage = Blueprint("init", __name__)

@landingPage.route("/")
def home():
    # ini akan cari ke ./templates/index.html
    return render_template("base.html")
