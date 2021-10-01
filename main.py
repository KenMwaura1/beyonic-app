from flask_migrate import Migrate
from app.commands import db_config, db
from app import create_app
from config import config_options

app = create_app('development')
app.config.from_object(config_options['development'])

db_config(app)
migrate = Migrate(app, db)


@app.cli.command("db")
def db():
    """command to migrate"""


if __name__ == '__main__':
    app.run()
