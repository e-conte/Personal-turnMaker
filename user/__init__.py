from flask import Blueprint, render_template
import common
import requests


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
    
    _information_list = common.business_third_line


    return render_template(f'{list(business_menu.keys())[2]}'+'.html',
                           _information_list=_information_list,
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )

@user_routes.route('/' +f'{href_menu[3]}', methods=['GET', 'POST'])
def fourth_line():
    try:
        _response = requests.get("https://dolarapi.com/v1/dolares")
        #print(response.json())
        for coin in _response.json():
            if coin['casa'] == 'blue':
                _dolar_blue = float(coin['venta'])
    except:
        try:
            _response_2 = requests.get("https://api.bluelytics.com.ar/v2/latest")
            _dolar_blue_2 = float(_response_2.json()['blue']['value_sell'])
        except:
            _dolar_blue = 0
            
    _business_prices = common.business_fourth_line_prices
          
    
    return render_template(f'{list(business_menu.keys())[3]}'+'.html',
                           _business_prices=_business_prices,
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )