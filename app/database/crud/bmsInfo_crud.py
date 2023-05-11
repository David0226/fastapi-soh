# user table에 대한 필요한 crud를 정의하는 파일

from sqlalchemy.orm import Session
from ..model import bms_info, bmsInfo_schema
from datetime import date

# Bms id 조건 조회
def get_bmsInfo(db: Session, bms_id: int):
    return db.query(bms_info.BmsInfo).filter(bms_info.BmsInfo.bmsId == bms_id).first()

# Bms id와 등록날짜 조건 조회
def get_bmsInfo_by_date(db: Session, bms_id: int, reg_date: date):
    return db.query(bms_info.BmsInfo).filter(bms_info.BmsInfo.bmsId == bms_id).filter(bms_info.BmsInfo.regDate == reg_date).first()

