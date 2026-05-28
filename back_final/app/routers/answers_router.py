from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Answer, Question
from app.schemas import AnswerCreate

router = APIRouter(
    prefix="/answers",
    tags=["Answers"]
)


@router.post("/")
def submit_answer(
        answer: AnswerCreate,
        db: Session = Depends(get_db)
):
    question = db.query(Question).filter(
        Question.id == answer.question_id
    ).first()

    is_correct = (
        question.correct_answer ==
        answer.answer
    )

    new_answer = Answer(
        game_id=answer.game_id,
        question_id=answer.question_id,
        team_id=answer.team_id,
        answer=answer.answer,
        is_correct=is_correct
    )

    db.add(new_answer)

    db.commit()

    return {
        "correct": is_correct
    }