from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Company, Employee, Client

router = APIRouter()

# Dependency για τη σύνδεση με τη βάση δεδομένων
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Δημιουργία εταιρίας
@router.post("/company/")
def create_company(name: str, vat_number: str, address: str, phone: str, email: str, db: Session = Depends(get_db)):
    existing_company = db.query(Company).filter(Company.vat_number == vat_number).first()
    if existing_company:
        raise HTTPException(status_code=400, detail="Company with this VAT number already exists.")
    
    new_company = Company(name=name, vat_number=vat_number, address=address, phone=phone, email=email)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

# Προσθήκη Εργαζομένου
@router.post("/employees/")
def add_employee(name: str, email: str, role: str, company_id: int, db: Session = Depends(get_db)):
    new_employee = Employee(name=name, email=email, role=role, company_id=company_id)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

# Προσθήκη Πελάτη
@router.post("/clients/")
def add_client(name: str, vat_number: str, contact_email: str, contact_phone: str, company_id: int, db: Session = Depends(get_db)):
    new_client = Client(name=name, vat_number=vat_number, contact_email=contact_email, contact_phone=contact_phone, company_id=company_id)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client
