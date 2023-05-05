from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from database import SessionLocal
from models import Question
from domain.question import question_schema,question_crud
router = APIRouter(
    prefix="/api/question",
)


@router.get("/list",response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):# 의존성 추가
    ''' 아래 역활로 변경 파일 닫기 자동화
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    db.close()
    '''

    ''' 다름 함수에서 호출
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    '''
    _question_list = question_crud.get_question_list(db)
    return _question_list