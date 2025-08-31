from flask import Blueprint, request, redirect, url_for, session, flash, jsonify, render_template
from flask import Flask
# from config import Config
from Controller.user.index import landingPage
from Controller.user.detail_rumah import detail_rumah
from Controller.admin.dashboard_admin import dashboard_admin
from Controller.admin.manajemen_admin import management_admin
from Controller.admin.laporan_admin import laporan_admin
from flask_cors import CORS
# Koneksi Database
from config import Config
from flask_mysqldb import MySQL



app = Flask(__name__,template_folder="../templates")

app.register_blueprint(landingPage)
app.register_blueprint(detail_rumah)
app.register_blueprint(dashboard_admin)
app.register_blueprint(management_admin)

app.register_blueprint(laporan_admin)


# Koneksi database
app.config.from_object(Config)
mysql = MySQL(app)

