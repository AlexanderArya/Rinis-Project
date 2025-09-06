from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()  # global instance

def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(Config)
    CORS(app)

    # Init MySQL sekali saja
    mysql.init_app(app)

    # Import blueprint setelah app siap
    from Controller.user.index import landingPage
    from Controller.user.detail_rumah import detail_rumah
    from Controller.admin.dashboard_admin import dashboard_admin
    from Controller.admin.manajemen_admin import management_admin
    from Controller.admin.laporan_admin import laporan_admin
    from Controller.admin.authentifikasi import authentifikasi
    
    app.register_blueprint(landingPage)
    app.register_blueprint(detail_rumah)
    app.register_blueprint(dashboard_admin)
    app.register_blueprint(management_admin)
    app.register_blueprint(laporan_admin)
    app.register_blueprint(authentifikasi)

    return app
