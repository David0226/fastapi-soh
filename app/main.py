from fastapi import FastAPI
from router import user_router, bmsInfo_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(bmsInfo_router.router)

@app.get("/")
def root():
        return {"message": "hello fast api"}
