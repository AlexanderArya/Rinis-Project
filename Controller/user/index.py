from flask import Blueprint, render_template

landingPage = Blueprint("init", __name__,template_folder="../templates")

@landingPage.route("/",methods=['GET'])
def init():
    return render_template('index.html')