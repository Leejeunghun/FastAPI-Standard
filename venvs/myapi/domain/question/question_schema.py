import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    '''. Question 모델은 Question 스키마로 자동으로 변환되지 않는다. 하지만 Quesiton 스키마에 다음처럼 orm_mode 항목을 True로 설정하면 Question 모델의 항목들이 자동으로 Question 스키마로 매핑된다.'''
    class Config:
        orm_mode = True