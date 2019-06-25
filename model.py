from flask_sqlalchemy import SQLAlchemy
from flask import jsonify 


db = SQLAlchemy()

class Vendor(db.Model):

	__tablename__ = "vendors"

	vend_id = db.Column(db.Integer, primary_key=True)
	vend_name = db.Column(db.Text)
	vend_address = db.Column(db.Text)
	user_vend_account = db.Column(db.String)

	def json(self):
		return { 
			'vend_id': self.vend_id,
			'vend_name': self.vend_name,
			'vend_address': self.vend_address,
			'user_vend_account': self.user_vend_account
			}

class Payment(db.Model):

	__tablename__ = "payments"

	pmt_id = db.Column(db.Integer, primary_key=True)
	pmt_amt = db.Column(db.Integer)
	pmt_date = db.Column(db.Text)
	pmt_type = db.Column(db.Integer, db.ForeignKey('payment_types.pmt_type_id'))

class PaymentType(db.Model):

	__tablename__ = "payment_types"

	pmt_type_id = db.Column(db.Integer, primary_key=True)
	pmt_details = db.Column(db.Text)

class Invoice(db.Model):

	__tablename__ = "invoices"

	inv_id = db.Column(db.Integer, primary_key=True)
	inv_number = db.Column(db.Text)
	inv_amt = db.Column(db.Integer)
	inv_vend_id = db.Column(db.Integer, db.ForeignKey('vendors.vend_id'))
	inv_pmt_id = db.Column(db.Integer, db.ForeignKey('payments.pmt_id'))

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