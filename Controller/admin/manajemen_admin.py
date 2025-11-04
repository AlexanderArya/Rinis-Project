from flask import Blueprint, render_template,jsonify
from utils.decorators import login_required
from Model.landingPageModel import LandingPageModel
from Model.adminModel import AdminModel 

management_admin = Blueprint("management_admin",__name__,template_folder="../templates")

@management_admin.route("/managemet")
@login_required
def admin_konten():
    return render_template('admin/management_konten.html')

@management_admin.route('/api/getAllData')
@login_required
def getAllData():
    print("sudah masuk ke sini")
    data = AdminModel.getAllDataProperties()
    print(data)
    return jsonify(data)