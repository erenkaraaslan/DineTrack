import os
from os import path

SESSION_COOKIE_NAME = 'login'

SECRET_KEY = 'fornowthisisthesecretkeyweshouldmakeitsomethingthatisactuallyrandom'

DATABASE_FILENAME = path.join(path.dirname(path.dirname(path.realpath(__file__))), "var", "dinetrack.sqlite3")

DEBUG = False