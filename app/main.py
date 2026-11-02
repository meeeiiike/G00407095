from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import engine, select
from app.database import get_db
from app.models import LoansDB, Base
from app.schemas import LoanCreate, LoanRead

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Equipment Loans")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/api/loans", status_code = status.HTTP_201_CREATED, response_model = LoanRead)
def add_loan(new_loan: LoanCreate, db: Session = Depends(get_db)):
    db_loan = LoansDB(**new_loan.model_dump())
    db.add(db_loan)
    try:
        db.commit()
        db.refresh(db_loan)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="DUPLICATE: Loan already exists",
        )
    return db_loan

@app.get("/api/loans/{loan_id}", status_code = status.HTTP_200_OK, response_model= LoanRead)
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan=db.get(LoansDB,loan_id)
    if db_loan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan Not Found",
        )
    return db_loan

@app.delete("/api/loans/{loan_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan=db.get(LoansDB,loan_id)
    if db_loan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan Not Found",
        )
    db.delete(db_loan)
    db.commit()
    return

