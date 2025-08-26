from flask import Blueprint, request, redirect, url_for, session, flash, jsonify, render_template
from flask import Flask
# from config import Config
from Controller.index import landingPage
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(landingPage,url_prefix='/')