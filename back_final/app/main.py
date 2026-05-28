from fastapi import FastAPI

from app.database import Base, engine

from app.routers.auth_router import router as auth_router
from app.routers.questions_router import router as questions_router
from app.routers.games_router import router as games_router
from app.routers.answers_router import router as answers_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quiz Backend API"
)

app.include_router(auth_router)
app.include_router(questions_router)
app.include_router(games_router)
app.include_router(answers_router)


@app.get("/")
def root():
    return {"message": "Quiz API"}