import os
from gears.finders import FileSystemFinder


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')


def register(environment):
    environment.finders.register(FileSystemFinder([ASSETS_DIR]))
