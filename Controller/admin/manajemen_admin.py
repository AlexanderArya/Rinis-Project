from flask import Blueprint, render_template, jsonify, request, session
from Controller import mysql
from utils.decorators import login_required
from Model.landingPageModel import LandingPageModel
from Model.adminModel import AdminModel
from Model.model_data import DatabaseCreate

management_admin = Blueprint("management_admin", __name__, template_folder="../templates")

@management_admin.route("/managemet")
@login_required
def admin_konten():
    return render_template('admin/management_konten.html')

@management_admin.route('/api/getAllData')
@login_required
def getAllData():
    data = AdminModel.getAllDataProperties()
    return jsonify(data)

@management_admin.route('/tambahData', methods=['POST'])
@login_required
def tambahan_data():
    try:
        data = request.get_json()
        data['id_penjual'] = session['user']['id_user']
        print(data)

        # Memanggil fungsi statis dari DatabaseCreate tanpa membuat objek
        result = DatabaseCreate.create_property(data)

        return jsonify(result)
    except Exception as e:
        # Jika terjadi error, tangani exception dan kirimkan pesan error
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': f'Gagal menambahkan properti: {str(e)}'}), 500
