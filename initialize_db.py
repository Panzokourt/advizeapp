import sys
import os

# Προσθήκη του backend στο PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from database.database import Base, engine
from models.models import Company, Employee, Client

print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Database created successfully.")
