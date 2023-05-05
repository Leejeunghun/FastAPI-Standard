import datetime

from pydantic import BaseModel,validator

from domain.answer.answer_schema import Answer

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    '''. Question 모델은 Question 스키마로 자동으로 변환되지 않는다. 하지만 Quesiton 스키마에 다음처럼 orm_mode 항목을 True로 설정하면 Question 모델의 항목들이 자동으로 Question 스키마로 매핑된다.'''
    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v