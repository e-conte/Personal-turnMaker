from flask import Blueprint, render_template, url_for
import common
import requests
import datetime
import locale



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

    _h3 = business_menu['first_line']
    
    _form_data = common.client_form_data
       
    _form_posible_date_time = common.business_schedule['Lunes a Viernes']['mañana']
    
    locale.setlocale(locale.LC_ALL, 'es_AR.UTF8')

    _range_of_days = common.range_of_date
    _today = datetime.date.today()
    _days = {}
    
    for i in range (_range_of_days):
        _date = _today + datetime.timedelta(days=i)
        _num_day = _date.day
        _week_day = " de "+_date.strftime("%B") + ", " + _date.strftime("%A")
        _days[_num_day] = _week_day

    return render_template(f'{list(business_menu.keys())[0]}' +'.html',
                           _h3 =_h3,
                           _form_data=_form_data,
                           _days=_days,
                           #_form_posible_date=_form_posible_date,
                           _form_posible_date_time=_form_posible_date_time,
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )

@user_routes.route('/' +f'{href_menu[0]}', methods=['GET', 'POST'])
def first_line_submit_form():
    
        
    return render_template(f'{list(business_menu.keys())[0]}' +'.html',
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )


@user_routes.route('/' +f'{href_menu[1]}', methods=['GET', 'POST'])
def second_line():

    _h3 = business_menu['second_line']
    
    return render_template(f'{list(business_menu.keys())[1]}'+'.html',
                           _h3 = _h3,
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )
    

@user_routes.route('/' +f'{href_menu[2]}', methods=['GET', 'POST'])
def third_line():
    
    _information_list = common.business_third_line
    _h3 = business_menu['third_line']
    
    return render_template(f'{list(business_menu.keys())[2]}'+'.html',
                           _h3=_h3,
                           _information_list=_information_list,
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )
    

@user_routes.route('/' +f'{href_menu[3]}', methods=['GET', 'POST'])
def fourth_line():

    _h3 = business_menu['fourth_line']

    try:
        _response = requests.get("https://dolarapi.com/v1/dolares",timeout = 3)
        #print(response.json())
        for coin in _response.json():
            if coin['casa'] == 'blue':
                _dolar_blue = float(coin['venta'])
    except:
        for attempt in range(3):
            try:
                _response_2 = requests.get("https://api.bluelytics.com.ar/v2/latest" ,timeout = 3)
                _dolar_blue_2 = float(_response_2.json()['blue']['value_sell'])
            except:
                _dolar_blue = 0
    
    _business_prices_in_uss = {}
    if _dolar_blue != 0:
        _moneda = "pesos"
        _business_prices = common.business_fourth_line_prices
        for  prices_in_uss in _business_prices:
            _business_prices_in_uss[prices_in_uss] = round(float(_business_prices[prices_in_uss]) * _dolar_blue, )
    else:
        _moneda = "dolares"
    
    return render_template(f'{list(business_menu.keys())[3]}'+'.html',
                           _h3=_h3,
                           _business_prices_in_uss=_business_prices_in_uss,
                           _moneda=_moneda,                  
                           business_info=business_info,
                           business_color=business_color,
                           href_menu=href_menu
                           )