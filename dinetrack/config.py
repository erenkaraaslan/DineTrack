import os
from os import path

SESSION_COOKIE_NAME = 'login'

DATABASE_FILENAME = path.join(path.dirname(path.realpath(__file__)), "var", "dinetrack.sqlite3")

DEBUG = False