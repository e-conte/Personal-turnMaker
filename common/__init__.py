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

business_third_line = [
    'Cambio de aceite y filtros',
    'Inspección de niveles de aceite',
    'Ajuste de válvulas',
    'Remplazo de bujías',
    'Cambio de fluidos de transmisión',
    'Cambio de pastillas las de freno',
    'Inspección y remplazo de batería',
    'Reparación de radiadores'
]       
# (ID min_padding fixes the height of this section)