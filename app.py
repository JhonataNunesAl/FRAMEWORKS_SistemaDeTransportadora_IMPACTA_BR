from config import app, db
from flask_migrate import Migrate, upgrade

from view.apartamento_view import apartamento_blueprint

migrate = Migrate(app, db)

app.register_blueprint(apartamento_blueprint, url_prefix='/api/apartamentos')

with app.app_context():
    upgrade()

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )