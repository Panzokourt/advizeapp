from fastapi import FastAPI
from routes import company_routes

app = FastAPI()

# Προσθήκη routes
app.include_router(company_routes.router)
