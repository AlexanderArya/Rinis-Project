from flask import Blueprint, render_template
from utils.decorators import login_required

laporan_admin = Blueprint("laporan_admin",__name__,template_folder="../templates")

@laporan_admin.route("/laporan",methods=['GET'])
@login_required
def init():
    return render_template("admin/laporan_admin.html")

