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

colors = ("white",
          "black",
          "red",
          "custom",
)

business_color = colors[2]

