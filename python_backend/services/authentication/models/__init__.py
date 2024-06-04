from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

from .base import Base
from .user import User

load_dotenv(find_dotenv())

'''

# This is a Python module that imports all the modules in the current directory and makes them available to be imported from the package.
module_files = glob.glob(join(dirname(__file__), "*.py"))
modules_inside_folder = []
for file in module_files:
	if isfile(file) and not file.endswith('__init__.py'):
		base = basename(file)[:-3]  # Remove .py
		modules_inside_folder.append(base)

__all__ = modules_inside_folder

# After all the modules have been programmatically imported, the __all__ variable is set to the list of module names. This is a list of strings that contains the names of all the modules in the
# current directory. This list is used to define the __all__ variable in the __init__.py file. This variable is used to define the list of modules that are imported when the package is imported.
# This is useful when you want to import all the modules in a package without having to import them one by one.

'''



# Now let's load the database

DATABASE_URL = getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
