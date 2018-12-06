from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from apps import create_app

app = create_app()
manager = Manager(app=app)

manager.add_command('start', Server())
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
