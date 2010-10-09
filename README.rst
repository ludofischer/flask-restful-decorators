Adds REST-like decorators to the Flask app.

Usage
-----
from flask import Flask
import restful_decorators
app = Flask(__name__)
restful_decorators.add_restful_decorators(app)

 Notes
-------
The decorators are added to one instance at a time.

License
-------
This package is licensed under the BSD license.
