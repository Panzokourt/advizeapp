from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.database import get_db
from backend.models.models import Client, Employee, Task

router = APIRouter()

@router.get("/stats")
def get_dashboard_stats(db: Session = Depends(get_db)):
    total_clients = db.query(Client).count()
    total_employees = db.query(Employee).count()
    active_tasks = db.query(Task).filter(Task.status == "active").count()
    return {
        "clients": total_clients,
        "employees": total_employees,
        "active_tasks": active_tasks
    }
