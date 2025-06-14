from flask import Flask
from flask_cors import CORS
from routes.reservaciones import reservaciones_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(reservaciones_bp, url_prefix="/reservaciones")

if __name__ == "__main__":
    app.run(debug=True)
