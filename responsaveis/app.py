# app.py
from flask import Flask
from responsavel_model import db
from routes import responsavel_bp
from flask_migrate import Migrate

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/app_responsaveis_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Registrar blueprints
app.register_blueprint(responsavel_bp)

# Inicializar extensões
db.init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__': 
    with app.app_context():
        db.create_all()
    app.run(debug=True)
