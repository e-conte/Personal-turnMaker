from flask import Blueprint

common_variables = Blueprint('common_variables', __name__)


#variables
business_info = {
    "name" : "Business Name",
    "slogan" : "Business Slogan",
    "direction" : "Business Direction",
    "phone" : "Business Phone",
    "email" : "Business Email",        
    }

business_menu = {
    "first_line" : "Sacar turno",
    "second_line" : "Consultar turno",
    "third_line" : "Nuestros servicios",
    "fourth_line" : "Tarifas",
}

#processing business menu information we get href for the menu
href_menu =[]
for line in business_menu.values():
    href_menu.append(line.lower().replace(" ", "_"))
# This will create href_menu for index.html

# style.css and #image_background and #menu_background should be changed/styled 

colors = {"white" : '/static/white_style.css',
          "black" : '/static/black_style.css',
          "red": '/static/red_style.css',
          "custom": '/static/custom_style.css',
}
business_color = colors['red']  # this is the font color/style


business_fourth_line_prices = {
    'Cambio de aceite y filtros': '15',
    'Inspección de niveles de aceite': '0',
    'Ajuste de válvulas': '10',
    'Remplazo de bujías':'5',
    'Cambio de fluidos de transmisión':'5',
    'Cambio de pastillas las de freno':'12',
    'Inspección y remplazo de batería':'60',
    'Reparación de radiadores': '20',
}

business_third_line = list(business_fourth_line_prices.keys())
# (ID min_padding fixes the height of this section)

