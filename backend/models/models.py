from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base

# Εταιρία
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    tasks = relationship("Task", back_populates="companies")
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
    tasks = relationship("Task", back_populates="employee")
    email = Column(String, unique=True, index=True)
    role = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="employees")

# Πελάτες
class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    tasks = relationship("Task", back_populates="client")
    vat_number = Column(String, unique=True, index=True)
    contact_email = Column(String)
    contact_phone = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="clients")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String, default="pending")
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)  # Διάρκεια σε δευτερόλεπτα

    # Foreign keys (παραδείγματα)
    client_id = Column(Integer, ForeignKey("clients.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))

    client = relationship("Client", back_populates="tasks")
    employee = relationship("Employee", back_populates="tasks")