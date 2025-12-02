from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Apartment(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True)
    number = Column(String)
    unit_type = Column(String)
    rent_amount = Column(Integer)

    # Relationship: One apartment has many tenants
    tenants = relationship("Tenant", back_populates="apartment")

    def __repr__(self):
        return f"<Apartment id={self.id} number={self.number} type={self.unit_type} rent={self.rent_amount}>"
