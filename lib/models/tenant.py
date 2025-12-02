from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    apartment_id = Column(Integer, ForeignKey("apartments.id"))

    # Relationship back to Apartment
    apartment = relationship("Apartment", back_populates="tenants")

    # Relationship to Payments
    payments = relationship("Payment", back_populates="tenant")

    def __repr__(self):
        return f"<Tenant id={self.id} name={self.name} phone={self.phone} apartment_id={self.apartment_id}>"
