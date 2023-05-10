from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.model import user_schema
from database.crud import user_crud
from database import db

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

# DB 세션을 가져오는 함수
def get_db():
    try:
        db_session = db.SessionLocal()
        yield db_session
    finally:
        db_session.close()

# API - create user
@router.post("/users", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return user_crud.create_user(db=db, user=user)

# API - update user
@router.put("/users/{user_id}", response_model=user_schema.User)
def update_user(user_id: int, user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.update_user(db=db, user_id=user_id, user=user)

# API - select user by user id
@router.get("/{user_id}", response_model=user_schema.User)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    Get a specific user by ID.
    """
    db_user = user_crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# API - delete user by user id
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_crud.delete_user(db, user_id=user_id)
    return {"message": "User deleted successfully"}