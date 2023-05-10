# user table에 대한 필요한 crud를 정의하는 파일

from sqlalchemy.orm import Session
from ..model import user, user_schema

def get_user(db: Session, user_id: int):
    return db.query(user.User).filter(user.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user.User).filter(user.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_schema.UserCreate):
    db_user = user.User(
        email=user.email, 
        hashed_password=user.hashed_password, 
        name=user.name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: user_schema.UserCreate):
    db_user = db.query(user.User).filter(user.User.id == user_id).first()
    db_user.name = user.name
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db.query(user.User).filter(user.User.id == user_id).delete()
    db.commit()