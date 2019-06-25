"""Utility file to seed database with data in seed_data folder"""

# from sqlalchemy import func
from model import Vendor, Payment, PaymentType, Invoice
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
        inv_number, inv_amt, inv_vend_id, inv_pmt_id = row.split(",")

        invoice = Invoice(inv_number=inv_number,
                    inv_amt=inv_amt,
                    inv_vend_id=inv_vend_id,
                    inv_pmt_id=inv_pmt_id)

        # We need to add to the session or it won't ever be stored
        db.session.add(invoice)

    # Once we're done, we should commit our work
    db.session.commit()


def load_vendors():
    """Load vendors from seed_data/vendor into database."""

    print("Vendors")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate vendors
    Vendor.query.delete()

    # Read vendor file and insert data
    for row in open("seed_data/vendor.txt"):
        row = row.rstrip()
        vend_name, vend_address, user_vend_account = row.split(",")

        vendor = Vendor(vend_name=vend_name,
                    vend_address=vend_address,
                    user_vend_account=user_vend_account)

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
        pmt_amt, pmt_date, pmt_type = row.split(",")

        payment = Payment(pmt_amt=pmt_amt,
                    pmt_date=pmt_date,
                    pmt_type=pmt_type)

        # We need to add to the session or it won't ever be stored
        db.session.add(payment)

    # Once we're done, we should commit our work
    db.session.commit()


def load_payment_types():
    """Load payment types from seed_data/pmt_type into database."""

    print("Payment Types")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate payment types
    PaymentType.query.delete()

    # Read payment file and insert data
    for row in open("seed_data/pmt_type.txt"):

        pmt_details = row.rstrip()

        pmt_type = PaymentType(pmt_details=pmt_details)

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