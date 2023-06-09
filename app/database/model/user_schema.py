# user table crud시 데이터 유효성 검증을 하는 파일 - Pydantic 모듈을 사용

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    userid: str

    class Config:
        orm_mode = True