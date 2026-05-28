from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class QuestionCreate(BaseModel):
    question: str

    option_a: str
    option_b: str
    option_c: str
    option_d: str

    correct_answer: str


class GameCreate(BaseModel):
    title: str


class AnswerCreate(BaseModel):
    game_id: int
    question_id: int
    team_id: int
    answer: str