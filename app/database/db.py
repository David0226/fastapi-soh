from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://<유저이름>:<비밀번호>@<호스트>/<데이터베이스이름>"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    echo=True, 
    pool_recycle=3600, 
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()