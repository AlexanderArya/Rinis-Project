from flask import request,Blueprint, redirect, session, url_for, render_template, json, send_from_directory
from Model.landingPageModel import LandingPageModel
import base64
import os


# Buat blueprint, bukan Flask app baru
landingPage = Blueprint("landingPage", __name__, static_folder='static')

@landingPage.route("/")
def home():
    data = LandingPageModel.get_property_with_image()   
    
    for item in data:
        if item['image_properties']:
            item['image_properties'] = base64.b64encode(item['image_properties']).decode("utf-8")
        else:
            item['image_properties'] = ""

    return render_template("user/index.html", data_json=json.dumps(data))

@landingPage.route("/errorr")
def errorExeption():
    return render_template("error/eror.html")

@landingPage.route("/logout", methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for("login.init"))

@landingPage.route("/getData")
def getData():
    data = LandingPageModel.get_property_with_image()
    return {"data": data}
