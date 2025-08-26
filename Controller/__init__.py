from flask import Blueprint, request, redirect, url_for, session, flash, jsonify, render_template
from flask import Flask
# from config import Config
from Controller.index import landingPage
from Controller.detail_rumah import detail_rumah
from Controller.admin.dashboard_admin import dashboard_admin
from Controller.admin.manajemen_admin import management_admin
from Controller.admin.laporan_admin import laporan_admin
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(landingPage)
app.register_blueprint(detail_rumah)
app.register_blueprint(dashboard_admin)
app.register_blueprint(management_admin)
app.register_blueprint(laporan_admin)