# user table을 정의하는 파일

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base


class Battery(Base):
    __tablename__ = "btry_info"

    bmsid = Column(String(50), primary_key=True)
    ts = Column(Integer, primary_key=True)
    packvol = Column(Integer)
    packcurr = Column(Integer)
    chgstat = Column(Integer)
