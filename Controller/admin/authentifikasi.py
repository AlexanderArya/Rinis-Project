from flask import Blueprint, render_template
from Model.authentifikasi import Authentification

authentifikasi = Blueprint("login",__name__,template_folder="../templates")

@authentifikasi.route("/login",methods=['GET'])
def init():
    return render_template("authentifikasi/login.html")

@authentifikasi.route("/register", methods=['GET'])
def register():
    return render_template("authentifikasi/register.html")

@authentifikasi.route("/registerUser", methods=["GET","POST"])
def registerUser():
    return ""