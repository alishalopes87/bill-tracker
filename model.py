from flask_sqlalchemy import SQLAlchemy
from flask import jsonify 


db = SQLAlchemy()

class Vendors(db.Model):

	__tablename__ = "vendors"

	vendor_id = db.Column(db.Integer, primary_key=True)
	vendor_name = db.Column(db.Text)
	billing_address = db.Column(db.Text)
	account_number = db.Column(db.String)

	def json(self):
		return { 
			'vendor_id': self.vendor_id,
			'vendor_name': self.vendor_name,
			'billing_address': self.billing_address,
			'account_number': self.account_number
			}

class Payment(db.Model):

	__tablename__ = "payments"

	payment_id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.Integer)
	date = db.Column(db.Text)
	payment_type = db.Column(db.Integer, db.ForeignKey('payment_types.payment_id'))

class Payment_type(db.Model):

	__tablename__ = "payment_types"

	payment_id = db.Column(db.Integer, primary_key=True)
	details = db.Column(db.Text)

class Invoice(db.Model):

	__tablename__ = "invoice"

	invoice_id = db.Column(db.Integer, primary_key=True)
	invoice_number = db.Column(db.Text)
	amount = db.Column(db.Integer)
	vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.vendor_id'))
	payment_id = db.Column(db.Integer, db.ForeignKey('payments.payment_id'))

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")