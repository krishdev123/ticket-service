
from sqlalchemy.orm import Session
from . import models, schemas


def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = models.Ticket(**ticket.model_dump())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_tickets(db: Session):
    return db.query(models.Ticket).all()


def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(
        models.Ticket.id == ticket_id
    ).first()


def get_customer_tickets(db: Session, customer_id: int):
    return db.query(models.Ticket).filter(
        models.Ticket.customer_id == customer_id
    ).all()


def update_ticket_status(db: Session, ticket_id: int, status: str):
    ticket = get_ticket(db, ticket_id)

    if ticket:
        ticket.status = status
        db.commit()
        db.refresh(ticket)

    return ticket
