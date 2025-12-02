# seed.py
from models import Base, engine

# Create all tables
print("Creating database tables...")
Base.metadata.create_all(engine)
print("Tables created successfully.")
