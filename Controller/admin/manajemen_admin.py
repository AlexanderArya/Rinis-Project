from flask import Blueprint, render_template

management_admin = Blueprint("management_admin",__name__,template_folder="../templates")

@management_admin.route("/managemet",methods=['GET'])
def init():
    return render_template('management_konten.html')