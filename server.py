from flask import Flask, jsonify,json
from model import *

app = Flask(__name__)


@app.route('/vendors')
def get_vendors():

	vendors = Vendors.query.all()
	json_vendors = []

	for vendor in vendors:
		vendor = vendor.json()
		json_vendors.append(vendor)

	return json.dumps(json_vendors)

# @app.route('/payment', methods=["POST"])
# def add_payment():



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar

    app.run(port=5000, host='0.0.0.0')