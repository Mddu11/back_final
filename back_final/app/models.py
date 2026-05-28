from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    first_name = Column(String)

    last_name = Column(String)

    email = Column(String, unique=True)

    hashed_password = Column(String)

    role = Column(String)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)

    question = Column(String)

    option_a = Column(String)
    option_b = Column(String)
    option_c = Column(String)
    option_d = Column(String)

    correct_answer = Column(String)


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    status = Column(String, default="waiting")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)

    game_id = Column(Integer)

    question_id = Column(Integer)

    team_id = Column(Integer)

    answer = Column(String)

    is_correct = Column(Boolean)