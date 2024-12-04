from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.database import get_db
from backend.models.models import Company  # Βεβαιώσου ότι το Company υπάρχει στο models

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)

@router.get("/")
def get_companies(db: Session = Depends(get_db)):
    """
    Retrieve all companies from the database.
    """
    companies = db.query(Company).all()
    return companies

@router.get("/{id}")
def get_company_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single company by ID.
    """
    company = db.query(Company).filter(Company.id == id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found.")
    return company

@router.post("/")
def create_company(name: str, vat_number: str, address: str, phone: str, email: str, db: Session = Depends(get_db)):
    """
    Create a new company.
    """
    new_company = Company(name=name, vat_number=vat_number, address=address, phone=phone, email=email)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

@router.put("/{id}")
def update_company(
    id: int,
    name: str = None,
    vat_number: str = None,
    address: str = None,
    phone: str = None,
    email: str = None,
    db: Session = Depends(get_db)
):
    """
    Update an existing company's details.
    """
    company = db.query(Company).filter(Company.id == id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found.")
    
    if name:
        company.name = name
    if vat_number:
        company.vat_number = vat_number
    if address:
        company.address = address
    if phone:
        company.phone = phone
    if email:
        company.email = email

    db.commit()
    db.refresh(company)
    return company

@router.delete("/{id}")
def delete_company(id: int, db: Session = Depends(get_db)):
    """
    Delete a company by ID.
    """
    company = db.query(Company).filter(Company.id == id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found.")
    
    db.delete(company)
    db.commit()
    return {"message": "Company deleted successfully"}
