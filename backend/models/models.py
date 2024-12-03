from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Εταιρία
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    vat_number = Column(String, unique=True, index=True)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    social_links = Column(String)  # JSON για πολλαπλά links

    employees = relationship("Employee", back_populates="company")
    clients = relationship("Client", back_populates="company")

# Εργαζόμενοι
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="employees")

# Πελάτες
class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    vat_number = Column(String, unique=True, index=True)
    contact_email = Column(String)
    contact_phone = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="clients")
