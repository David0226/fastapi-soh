# user table crud시 데이터 유효성 검증을 하는 파일 - Pydantic 모듈을 사용
from datetime import date
from pydantic import BaseModel, validator

class BmsInfo(BaseModel):
    bmsId: int
    temp: int
    cellVol: int
    batterySoh :int
    regDate : date

    # cell voltage 값 검증
    @validator('cellVol')
    def validate_cell_vol(cls, value):
        if value < 3.4 or value > 3.7:
            raise ValueError('cellVol must be between 3.4 and 3.7')
        return value        
         
    class Config:
        orm_mode = True        
        

        