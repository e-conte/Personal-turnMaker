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
# De style.css #image_background + #menu_background 

colors = {"white" : '/static/white_style.css',
          "black" : '/static/black_style.css',
          "red": '/static/red_style.css',
          "custom": '/static/custom_style.css',
}

business_color = colors['white']  # this is the font color/style

