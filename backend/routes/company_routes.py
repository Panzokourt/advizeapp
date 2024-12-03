from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.database import SessionLocal
from backend.models.models import Company


router = APIRouter()

# Dependency για τη σύνδεση με τη βάση δεδομένων
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route για τη δημιουργία νέας εταιρείας
@router.post("/companies/")
def create_company(name: str, email: str, phone: str, address: str, db: Session = Depends(get_db)):
    new_company = Company(name=name, email=email, phone=phone, address=address)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company
