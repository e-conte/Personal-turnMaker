from flask import Blueprint

common_variables = Blueprint('common_variables', __name__)

#variables
business_info = {
    "name" : "<h1>Business Name</h1>",
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
# faltan style.css #image_background + colores

business_color = ("white",  #change from user
                  "black",
                  "red",
                  "custom",
) 