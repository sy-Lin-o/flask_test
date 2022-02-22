from flask import render_template
from flask import Flask
from flask_api import app
from flask import request
import logging
from logging.config import dictConfig

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

# if __name__ == '__main__':
#     app.run(debug = True)