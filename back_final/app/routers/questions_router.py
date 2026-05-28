from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Question
from app.schemas import QuestionCreate

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


@router.post("/")
def create_question(
        question: QuestionCreate,
        db: Session = Depends(get_db)
):
    db_question = Question(**question.dict())

    db.add(db_question)

    db.commit()

    return db_question


@router.get("/")
def get_questions(
        db: Session = Depends(get_db)
):
    return db.query(Question).all()