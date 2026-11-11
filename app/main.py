
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db
from .customer_client import validate_customer

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Telecom Ticket Service",
    description="Ticket Management Microservice",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {"status": "healthy", "service": "ticket-service"}


@app.post("/tickets", response_model=schemas.TicketResponse, status_code=201)
def create_ticket(
    ticket: schemas.TicketCreate,
    db: Session = Depends(get_db)
):
    validate_customer(ticket.customer_id)
    return crud.create_ticket(db, ticket)


@app.get("/tickets", response_model=list[schemas.TicketResponse])
def list_tickets(db: Session = Depends(get_db)):
    return crud.get_tickets(db)


@app.get("/tickets/customer/{customer_id}",
         response_model=list[schemas.TicketResponse])
def customer_tickets(customer_id: int, db: Session = Depends(get_db)):
    validate_customer(customer_id)
    return crud.get_customer_tickets(db, customer_id)


@app.get("/tickets/{ticket_id}", response_model=schemas.TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


@app.patch("/tickets/{ticket_id}/status",
           response_model=schemas.TicketResponse)
def update_status(
    ticket_id: int,
    update: schemas.TicketStatusUpdate,
    db: Session = Depends(get_db)
):
    ticket = crud.update_ticket_status(db, ticket_id, update.status)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket
