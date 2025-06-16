from flask import Flask
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://my_database_0upx_user:b08KI2ByRKUXQCchx9UkkxnViHO8k59B@dpg-d15vd8p5pdvs73e30b50-a.oregon-postgres.render.com/my_database_0upx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route ('/')
def home():
    return "API running"


if __name__ == "__main__":
    app.run(debug=True)

