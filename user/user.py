from flask import Blueprint, render_template
from common import common

user_routes = Blueprint('user_routes', __name__)

global business_info, business_color

business_info = common.business_info
business_color = common.business_color

@user_routes.route('/', methods=['GET', 'POST'])
def index():

    _index_menu = {}
    _href_menu = []
    _index_menu = common.business_menu

    for line in common.business_menu.values():
        _href_menu.append(line.lower().replace(" ", "_"))
           
#    _href_menu = _href_menu.append(value.lower().replace(" ", "_"))

    return render_template('index.html',
                           _index_menu=_index_menu,
                           _href_menu=_href_menu,
                           business_info=business_info,
                           business_color=business_color,
                           )
    


    
@user_routes.route('/{}.format(business_info["first_line"])', methods=['GET', 'POST'])
def first_line():

    return render_template('index.html',
                           _index_menu=common.business_menu,
                           business_info=business_info,
                           business_color=business_color
                           )