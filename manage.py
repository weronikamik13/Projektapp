from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from setup import app, db

app = app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
