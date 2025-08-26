from flask import Blueprint, render_template

laporan_admin = Blueprint("laporan_admin",__name__,template_folder="../templates")

@laporan_admin.route("/laporan",methods=['GET'])
def init():
    return render_template("laporan_admin.html")