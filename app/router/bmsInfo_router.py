from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.model import bmsInfo, bmsInfo_schema
from database.crud import bmsInfo_crud
from database import db
from datetime import date

router = APIRouter(
    prefix='/bmsinfo',
    tags=['bmsinfo'],
)

# DB 세션을 가져오는 함수
def get_db():
    try:
        db_session = db.SessionLocal()
        yield db_session
    finally:
        db_session.close()

# API - Get bmsInfo data by {bms id}
@router.get("/{bmd_id}", response_model=bmsInfo_schema.BmsInfo)
def get_bmsInfo(bms_id: int, db: Session = Depends(get_db)):
    """
    Get a specific user by ID.
    """
    getBms = bmsInfo_crud.get_bmsInfo(db=db, bms_id=bms_id)
    if getBms is None:
        raise HTTPException(status_code=404, detail="Bms Data not found")
    return getBms

# API - Get bmsInfo data by {bms id & date}
@router.get("/{bms_id}/{reg_date}", response_model=bmsInfo_schema.BmsInfo)
def get_bmsInfo(bms_id: int, reg_date: date, db: Session = Depends(get_db)):
    """
    Get a specific user by ID.
    """
    getBms = bmsInfo_crud.get_bmsInfo_by_date(db=db, bms_id=bms_id, reg_date=reg_date)
    if getBms is None:
        raise HTTPException(status_code=404, detail="Bms Data not found")
    return getBms

# API - Get Predicted SOH Value 
@router.get("/predsoh/{bms_id}/{reg_date}", response_model=bmsInfo_schema.BmsInfo)
def get_bmsInfo(bms_id: int, reg_date: date, db: Session = Depends(get_db)):
    """
    Get a specific user by ID.
    """
    getBms = bmsInfo_crud.get_bmsInfo_by_date(db=db, bms_id=bms_id, reg_date=reg_date)
    if getBms is None:
        raise HTTPException(status_code=404, detail="Bms Data not found")
    else :
        predictedSoh = getBms["predictedt_Soh"]
        return predictedSoh