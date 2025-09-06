from flask import Blueprint, render_template
from Model.landingPageModel import LandingPageModel
import base64

# Buat blueprint, bukan Flask app baru
landingPage = Blueprint("landingPage", __name__)

@landingPage.route("/")
def home():
    data = LandingPageModel.get_property_with_imageA()   
    # Ubah semua image_properties menjadi base64 string
    for item in data:
        if item['image_properties']:  # pastikan ada gambar
            item['image_properties'] = base64.b64encode(item['image_properties']).decode("utf-8")
        else:
            item['image_properties'] = ""  # jika kosong, kasih string kosong
    
    # Render template, langsung pakai data
    return render_template("user/index.html",data=data)

@landingPage.route("/testing")
def testingController():
    return render_template('test.html')

@landingPage.route("/getData")
def getData():
    # contoh kalau mau ambil data JSON dari model
    data = LandingPageModel.get_property_with_imageA()
    return {"data": data}
