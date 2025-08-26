from flask import Blueprint, render_template
detail = Blueprint('detail',__name__,template_folder="../templates")

@detail.route("/detail",methods=['GET'])
def detail():
    return render_template('detail.html')