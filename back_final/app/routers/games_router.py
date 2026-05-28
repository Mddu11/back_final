from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Game
from app.schemas import GameCreate

from app.redis_client import redis_client

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)


@router.post("/")
def create_game(
        game: GameCreate,
        db: Session = Depends(get_db)
):
    db_game = Game(title=game.title)

    db.add(db_game)

    db.commit()

    return db_game


@router.post("/{game_id}/start")
def start_game(game_id: int):
    redis_client.publish(
        f"quiz_game_{game_id}",
        "Game started"
    )

    return {"message": "Game started"}