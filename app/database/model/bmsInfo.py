# user table을 정의하는 파일

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..db import Base

class BmsInfo(Base):
    __tablename__ = "bms_info"

    bmsId = Column(Integer, primary_key=True, index=True)
    temp = Column(Integer)
    cellVol = Column(Integer)
    soh = Column(Integer)
    predictedt_Soh = Column(Integer)
    regDate = Column(DateTime, server_default=func.now())



