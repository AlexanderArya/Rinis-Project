from flask import Blueprint, render_template

detail_rumah = Blueprint("detail_rumah",__name__,template_folder="../templates")

@detail_rumah.route("/detail",methods=['GET'])
def detail():
    return render_template('detail.html')