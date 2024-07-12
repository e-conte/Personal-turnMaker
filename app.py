from flask import Flask, render_template, request, url_for, redirect, flash
#blueprints
from user import user_routes
from business import business_routes
from common import common_variables


app = Flask(__name__)
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(business_routes, url_prefix='/business')
app.register_blueprint(common_variables, url_prefix='/common')
app.config['TEMPLATE_FOLDER'] = 'templates' #Nueva configuración
app.config['SECRET_KEY'] = 'una-clave-secreta'
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('user_routes.index'))

if __name__ == '__main__':
    app.run(debug=True)