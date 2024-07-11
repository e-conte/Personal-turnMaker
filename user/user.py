from flask import Blueprint, render_template
from common import common

user_routes = Blueprint('user_routes', __name__)

global business_info, business_color
business_info = common.business_info
business_color = common.business_color(0) #change from here

@user_routes.route('/', methods=['GET', 'POST'])
def index():
    _index_menu =  {}
    _index_menu = common.business_menu
    color = "255,0,0"
    print(_index_menu)
    return render_template('index.html',
                           _index_menu=_index_menu,
                           business_info=business_info,
                           business_color=business_color
                           )
