from flask import Blueprint, render_template
from common import common

user_routes = Blueprint('user_routes', __name__)

# imported variables
business_info = common.business_info
business_color = common.business_color
business_menu = common.business_menu
href_menu = common.href_menu


@user_routes.route('/', methods=['GET', 'POST'])
def index():

    _index_menu = {}
    _index_menu = common.business_menu          
    
    return render_template('index.html',
                           _index_menu=_index_menu,
                           href_menu=href_menu,
                           business_info=business_info,
                           business_color=business_color,
                           ) 
   
@user_routes.route('/' +f'{href_menu[0]}', methods=['GET', 'POST'])
def first_line():

    return render_template(f'{list(business_menu.keys())[0]}' +'.html',
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )

@user_routes.route('/' +f'{href_menu[1]}', methods=['GET', 'POST'])
def second_line():

    return render_template(f'{list(business_menu.keys())[1]}'+'.html',
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )

@user_routes.route('/' +f'{href_menu[2]}', methods=['GET', 'POST'])
def third_line():

    return render_template(f'{list(business_menu.keys())[2]}'+'.html',
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )

@user_routes.route('/' +f'{href_menu[3]}', methods=['GET', 'POST'])
def fourth_line():

    return render_template(f'{list(business_menu.keys())[3]}'+'.html',
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )