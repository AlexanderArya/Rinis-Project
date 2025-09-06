from flask import Blueprint, render_template

dashboard_admin = Blueprint("dashboard_admin",__name__,template_folder="../templates")

@dashboard_admin.route("/dashboard",methods=['GET'])
def init():
    return render_template("admin/dashboard_admin.html")