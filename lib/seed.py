# seed.py
from models import Base, engine, session
from models.apartment import Apartment
from models.tenant import Tenant
from models.payment import Payment

print("Creating tables...")
Base.metadata.create_all(engine)

print("Seeding sample data...")

# Sample Apartments
apt1 = Apartment(number="101", unit_type="1 Bedroom", rent_amount=15000)
apt2 = Apartment(number="102", unit_type="Bedsitter", rent_amount=8000)

session.add_all([apt1, apt2])
session.commit()

# Sample Tenants
tenant1 = Tenant(name="Abdirahan Mohamed", phone="0754675434", apartment_id=apt1.id)
tenant2 = Tenant(name="Albert Byrone", phone="0798765432", apartment_id=apt2.id)

session.add_all([tenant1, tenant2])
session.commit()

# Sample Payments
payment1 = Payment(amount=15000, date_paid="2025-02-01", tenant_id=tenant1.id)
payment2 = Payment(amount=8000, date_paid="2025-02-03", tenant_id=tenant2.id)

session.add_all([payment1, payment2])
session.commit()

print("Seeding completed successfully!")
