from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    date_paid = Column(String)
    tenant_id = Column(Integer, ForeignKey("tenants.id"))

    # Relationship back to Tenant
    tenant = relationship("Tenant", back_populates="payments")

    def __repr__(self):
        return f"<Payment id={self.id} amount={self.amount} date={self.date_paid} tenant_id={self.tenant_id}>"
