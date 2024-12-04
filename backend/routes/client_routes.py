from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.database import get_db
from backend.models.models import Client  # Βεβαιώσου ότι το Client υπάρχει στο models

router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
)

@router.get("/")
def get_clients(db: Session = Depends(get_db)):
    """
    Retrieve all clients from the database.
    """
    clients = db.query(Client).all()
    return clients

@router.get("/{id}")
def get_client_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single client by ID.
    """
    client = db.query(Client).filter(Client.id == id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found.")
    return client

@router.put("/{id}")
def update_client(
    id: int,
    name: str = None,
    vat_number: str = None,
    contact_email: str = None,
    contact_phone: str = None,
    db: Session = Depends(get_db)
):
    """
    Update an existing client's details.
    """
    client = db.query(Client).filter(Client.id == id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found.")
    
    if name:
        client.name = name
    if vat_number:
        client.vat_number = vat_number
    if contact_email:
        client.contact_email = contact_email
    if contact_phone:
        client.contact_phone = contact_phone

    db.commit()
    db.refresh(client)
    return client

@router.delete("/{id}")
def delete_client(id: int, db: Session = Depends(get_db)):
    """
    Delete a client by ID.
    """
    client = db.query(Client).filter(Client.id == id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found.")
    
    db.delete(client)
    db.commit()
    return {"message": "Client deleted successfully"}
