# functions.py
from models import session
from models.apartment import Apartment
from models.tenant import Tenant
from models.payment import Payment

# APARTMENT FUNCTIONS


def create_apartment(number, unit_type, rent_amount):
    apartment = Apartment(number=number, unit_type=unit_type, rent_amount=rent_amount)
    session.add(apartment)
    session.commit()
    return apartment

def list_apartments():
    return session.query(Apartment).all()

def find_apartment(apartment_id):
    return session.query(Apartment).get(apartment_id)

def delete_apartment(apartment_id):
    apartment = find_apartment(apartment_id)
    if apartment:
        session.delete(apartment)
        session.commit()
        return True
    return False

def get_apartment_tenants(apartment_id):
    apartment = find_apartment(apartment_id)
    if apartment:
        return apartment.tenants
    return None

def update_apartment(apartment_id, number=None, unit_type=None, rent_amount=None):
    apartment = find_apartment(apartment_id)
    if apartment:
        if number:
            apartment.number = number
        if unit_type:
            apartment.unit_type = unit_type
        if rent_amount:
            apartment.rent_amount = rent_amount

        session.commit()
        return apartment
    return None



# ---------------------------
# TENANT FUNCTIONS
# ---------------------------

def create_tenant(name, phone, apartment_id):
    tenant = Tenant(name=name, phone=phone, apartment_id=apartment_id)
    session.add(tenant)
    session.commit()
    return tenant

def list_tenants():
    return session.query(Tenant).all()

def find_tenant(tenant_id):
    return session.query(Tenant).get(tenant_id)

def delete_tenant(tenant_id):
    tenant = find_tenant(tenant_id)
    if tenant:
        session.delete(tenant)
        session.commit()
        return True
    return False

def get_tenant_payments(tenant_id):
    tenant = find_tenant(tenant_id)
    if tenant:
        return tenant.payments
    return None

def update_tenant(tenant_id, name=None, phone=None, apartment_id=None):
    tenant = find_tenant(tenant_id)
    if tenant:
        if name:
            tenant.name = name
        if phone:
            tenant.phone = phone
        if apartment_id:
            tenant.apartment_id = apartment_id

        session.commit()
        return tenant
    return None


# ---------------------------
# PAYMENT FUNCTIONS
# ---------------------------

def create_payment(amount, date_paid, tenant_id):
    payment = Payment(amount=amount, date_paid=date_paid, tenant_id=tenant_id)
    session.add(payment)
    session.commit()
    return payment

def list_payments():
    return session.query(Payment).all()

def find_payment(payment_id):
    return session.query(Payment).get(payment_id)

def delete_payment(payment_id):
    payment = find_payment(payment_id)
    if payment:
        session.delete(payment)
        session.commit()
        return True
    return False

def update_payment(payment_id, amount=None, date_paid=None):
    payment = find_payment(payment_id)
    if payment:
        if amount:
            payment.amount = amount
        if date_paid:
            payment.date_paid = date_paid

        session.commit()
        return payment
    return None
