from flask import Flask, jsonify
from model import *

app = Flask(__name__)


@app.route('/vendors')
def get_vendors():

	vendors = Vendor.query.all()

	return jsonify(**vendors)

# @app.route('/payment', methods=["POST"])
# def add_payment():



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')