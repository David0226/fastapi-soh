# user table에 대한 필요한 crud를 정의하는 파일

from sqlalchemy.orm import Session
from ..model import battery, battery_schema


def get_datas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(battery.Battery).offset(skip).limit(limit).all()
