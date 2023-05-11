# user table을 정의하는 파일

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base
<<<<<<< HEAD

=======
>>>>>>> refs/remotes/origin/master

class User(Base):
    __tablename__ = "test_user"

    userid = Column(String(50), primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(100))
