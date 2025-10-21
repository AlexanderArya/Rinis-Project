from flask import Blueprint, render_template,request, jsonify, session
from Model.authentifikasi import Authentification
from utils.decorators import login_required

authentifikasi = Blueprint("login",__name__,template_folder="../templates")

@authentifikasi.route("/login",methods=['GET'])
def init():
    return render_template("authentifikasi/login.html")

@login_required
@authentifikasi.route("/register", methods=['GET'])
def register():
    return render_template("authentifikasi/register.html")

@authentifikasi.route("/loginUser", methods=["POST"])
def loginUser():
    data = request.get_json() 
    email = data.get('email')
    password = data.get('password')

    result = Authentification.login_user_admin(email, password)
    if result['success']:
        # simpan data user ke session
        session['user'] = {
            "id_user": result['id_user'],
            "name": result['name'],
            "email": result['email'],
            "role": result['role']
        }
        return jsonify({"status": "ok", "user": session['user']})
    else:
        return jsonify({"status": "nok", "message": result['message']})