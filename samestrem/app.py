import os
from flask_extended import Flask
from flask import jsonify, render_template, url_for
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
    return render_template('index.html',title="Home")


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
