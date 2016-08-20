print "I am right here"

import os
from flask_extended import Flask
from flask import jsonify
import logging
from logging import FileHandler, Formatter

app = Flask(__name__)

app.config.from_yaml(os.path.join(app.root_path, 'config.yml'))
if os.path.isfile(os.path.join(app.root_path, "local_config.yml")):
    app.config.from_yaml(os.path.join(app.root_path, 'local_config.yml'))


from errorhandler import *


from routes.info import info
app.register_blueprint(info)


format = Formatter(
    'SAMESTREM: %(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
)
error_handler = FileHandler(app.config['LOG_FILE'])
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(format)
app.logger.addHandler(error_handler)


@app.route('/')
def index():
    """
    API index endpoint
    """
    message = "You hit the API index! Excellent!"
    response = jsonify(message=message)
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
