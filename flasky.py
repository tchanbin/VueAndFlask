import os
import click
from flask_migrate import Migrate
from app import create_app, db

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell,Server


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict( )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

manager.add_command("runserver", Server(host="0.0.0.0",port="5000"))

from app.models import User, Role, Permission

if __name__ == '__main__':
    # manager.run(host="0.0.0.0",port="5000")
    manager.run()

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, Follow=Follow, Role=Role,
#                 Permission=Permission, Post=Post, Comment=Comment)
#
#
# @app.cli.command()
# @click.argument('test_names', nargs=-1)
# def test(test_names):
#     """Run the unit tests."""
#     import unittest
#     if test_names:
#         tests = unittest.TestLoader().loadTestsFromNames(test_names)
#     else:
#         tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)
