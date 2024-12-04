from fastapi import FastAPI
from backend.routes import company_routes, employee_routes, client_routes, dashboard_routes

app = FastAPI()

app.include_router(company_routes.router, prefix="/company", tags=["Company"])
app.include_router(employee_routes.router, prefix="/employees", tags=["Employees"])
app.include_router(client_routes.router, prefix="/clients", tags=["Clients"])
app.include_router(dashboard_routes.router, prefix="/dashboard", tags=["Dashboard"])
