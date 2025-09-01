from flask import Blueprint, render_template, current_app
from Model.landingPageModel import LandingPageModel

landingPage = Blueprint("init", __name__)

@landingPage.route("/")
def home():
    model = LandingPageModel(current_app)
    data = model.get_property_with_image()
    return render_template("index.html")

@landingPage.route("/getData")
def getData():
    pass

    # return data