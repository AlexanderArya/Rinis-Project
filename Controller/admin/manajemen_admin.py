from flask import Blueprint, render_template
from utils.decorators import login_required

management_admin = Blueprint("management_admin",__name__,template_folder="../templates")

@management_admin.route("/managemet")
@login_required
def admin_konten():
    return render_template('admin/management_konten.html')