"""Utility file to seed database with data in seed_data/"""

from datetime import datetime
# from sqlalchemy import func
from model import Vendors, Payment, Payment_type, Invoice
from model import connect_to_db, db

from server import app

def load_invoices():
    """Load invoices from seed_data/invoice into database."""

    print("Invoices")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate invoices
    Invoice.query.delete()

    # Read invoice file and insert data
    for row in open("seed_data/invoice.txt"):
        row = row.rstrip()
        vendor_id, invoice_number, amount, payment_id = row.split(",")

        invoice = Invoice(vendor_id=vendor_id,
                    invoice_number=invoice_number,
                    amount=amount,
                    payment_id=payment_id)

        # We need to add to the session or it won't ever be stored
        db.session.add(invoice)

    # Once we're done, we should commit our work
    db.session.commit()


def load_vendors():
    """Load vendors from seed_data/vendor into database."""

    print("Vendors")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate vendors
    Vendors.query.delete()

    # Read vendor file and insert data
    for row in open("seed_data/vendor.txt"):
        row = row.rstrip()
        vendor_name, billing_address, account_number = row.split(",")

        vendor = Vendors(vendor_name=vendor_name,
                    billing_address=billing_address,
                    account_number=account_number)

        # We need to add to the session or it won't ever be stored
        db.session.add(vendor)

    # Once we're done, we should commit our work
    db.session.commit()


def load_payments():
    """Load vendors from seed_data/payment into database."""

    print("Payments")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate payments
    Payment.query.delete()

    # Read payment file and insert data
    for row in open("seed_data/payment.txt"):
        row = row.rstrip()
        amount, date, payment_type = row.split(",")

        payment = Payment(amount=amount,
                    date=date,
                    payment_type=payment_type)

        # We need to add to the session or it won't ever be stored
        db.session.add(payment)

    # Once we're done, we should commit our work
    db.session.commit()


def load_payment_types():
    """Load payment types from seed_data/pmt_type into database."""

    print("Payment Types")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate payment types
    Payment_type.query.delete()

    # Read payment file and insert data
    for row in open("seed_data/pmt_type.txt"):
        row = row.rstrip()
        # details = row.split(",")
        details = row
        pmt_type = Payment_type(details=details)

        # We need to add to the session or it won't ever be stored
        db.session.add(pmt_type)

    # Once we're done, we should commit our work
    db.session.commit()



if __name__ == "__main__":

    connect_to_db(app)

    # In case tables haven't been created, create them

    db.create_all()

    load_invoices()

    load_vendors()

    load_payments()

    load_payment_types()