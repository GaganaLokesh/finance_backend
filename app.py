from flask import Flask
from config import Config
from models import db
from routes.user_routes import routes
from routes.finance_routes import finance_routes
from routes.dashboard_routes import dashboard_routes
from exceptions import ResourceNotFound

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Registering routes
app.register_blueprint(routes)
app.register_blueprint(finance_routes)
app.register_blueprint(dashboard_routes)

# Exception handling
@app.errorhandler(ResourceNotFound)
def handle_not_found(e):
    return {"error": str(e)}, 404

@app.errorhandler(ValueError)
def handle_value_error(e):
    return {"error": str(e)}, 400

@app.errorhandler(Exception)
def handle_general(e):
    return {"error": "Something went wrong"}, 500


# Create tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)