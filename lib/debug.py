# debug.py
from models import session
from models.apartment import Apartment
from models.tenant import Tenant
from models.payment import Payment

# List all apartments
print("\nApartments:")
for apt in session.query(Apartment).all():
    print(apt)

# List all tenants
print("\nTenants:")
for t in session.query(Tenant).all():
    print(t)

# List all payments
print("\nPayments:")
for p in session.query(Payment).all():
    print(p)
