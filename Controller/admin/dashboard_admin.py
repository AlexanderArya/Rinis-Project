from flask import Blueprint, render_template, session, jsonify, request
from datetime import datetime
from utils.decorators import login_required
from Model.landingPageModel import LandingPageModel
from Model.viewerModel import ViewerPage

dashboard_admin = Blueprint("dashboard_admin", __name__, template_folder="../templates")

@dashboard_admin.route("/dashboard", methods=['GET'])
@login_required
def init():
    nama = session['user']['name']
    hour = datetime.now().hour

    if 5 <= hour < 12:
        greeting = "Selamat Pagi"
    elif 12 <= hour < 15:
        greeting = "Selamat Siang"
    elif 15 <= hour < 18:
        greeting = "Selamat Sore"
    else:
        greeting = "Selamat Malam"

    return render_template("admin/dashboard_admin.html", data=nama, greeting=greeting)

@dashboard_admin.route("/DataDashboard", methods=['GET'])
def getDataDashboard():
    data = {
        "message": "Data Sudah ada",
        "disewakan": len(LandingPageModel.get_disewakan_30_hari()),
        "terjual": len(LandingPageModel.get_dijual_30_hari()),
        "tersedia": len(LandingPageModel.get_tersedia()),
        "total_properti": len(LandingPageModel.get_property_with_image())
    }
    
    return jsonify({"data":data})

@dashboard_admin.route("/api/available")
def getDataAvailable():
    data = LandingPageModel.get_data_available()
    return jsonify(data)

# done 
@dashboard_admin.route("/api/type_chart")
def getDataChart():
    data =LandingPageModel.get_result_count_data()
    return jsonify(data)

@dashboard_admin.route("/api/sales")
def getStatsData():
    data = LandingPageModel.getStatsDatabyMonth()
    return jsonify(data)

@dashboard_admin.route('/api/totalViews')
def getView():
    view_count, transaksi_count, presentase = ViewerPage.get_view_count('/', session['user']['id_user'])

    dataTotal = {
        "view_count":view_count,
        "Total_Jual":transaksi_count,
        "presentase":presentase
    }
    
    return jsonify(dataTotal)

@dashboard_admin.route('/api/logs')
def getDataViewer():
    data = LandingPageModel.get_viewer_logs()
    return jsonify(data)

@dashboard_admin.route('/api/hargaMahal')
def hargaMahal():
    data = LandingPageModel.harga_termahal()
    print(data)
    return jsonify(data)
