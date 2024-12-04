from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.database import get_db
from backend.models.models import Employee  # Βεβαιώσου ότι το Employee υπάρχει στο models

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)

@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    """
    Retrieve all employees from the database.
    """
    employees = db.query(Employee).all()
    return employees

@router.get("/{id}")
def get_employee_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single employee by ID.
    """
    employee = db.query(Employee).filter(Employee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found.")
    return employee

@router.post("/")
def create_employee(name: str, position: str, email: str, phone: str, db: Session = Depends(get_db)):
    """
    Create a new employee.
    """
    new_employee = Employee(name=name, position=position, email=email, phone=phone)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@router.put("/{id}")
def update_employee(
    id: int,
    name: str = None,
    position: str = None,
    email: str = None,
    phone: str = None,
    db: Session = Depends(get_db)
):
    """
    Update an existing employee's details.
    """
    employee = db.query(Employee).filter(Employee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found.")
    
    if name:
        employee.name = name
    if position:
        employee.position = position
    if email:
        employee.email = email
    if phone:
        employee.phone = phone

    db.commit()
    db.refresh(employee)
    return employee

@router.delete("/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    """
    Delete an employee by ID.
    """
    employee = db.query(Employee).filter(Employee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found.")
    
    db.delete(employee)
    db.commit()
    return {"message": "Employee deleted successfully"}
