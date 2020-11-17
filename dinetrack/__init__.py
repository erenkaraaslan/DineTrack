from flask import Flask

app = Flask(__name__)

app.config.from_object('dinetrack.config')

app.config.from_envvar('DINETRACK_SETTINGS', silent=True)

import dinetrack.views 