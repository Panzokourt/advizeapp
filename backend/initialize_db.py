from database import Base, engine
from models import Company, Employee, Client

print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Database created successfully.")
