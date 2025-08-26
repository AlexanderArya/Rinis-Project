from flask import Blueprint, request, redirect, url_for, session, flash, jsonify, render_template
from flask import Flask
# from config import Config
from Controller.index import landingPage
from Controller.detail_rumah import detail_rumah
from flask_cors import CORS

app = Flask(__name__)


app.register_blueprint(landingPage)
app.register_blueprint(detail_rumah)