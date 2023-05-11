from fastapi import FastAPI
<<<<<<< HEAD
from router import user_router
from os import path

import soh.soh_service as service
=======
from router import user_router, bmsInfo_router
>>>>>>> refs/remotes/origin/master

app = FastAPI()

app.include_router(user_router.router)
app.include_router(bmsInfo_router.router)


@app.get("/")
def root():
    return {"message": "hello fast api"}


def main():
    print("main")
    service.SohService(path.dirname( path.abspath(__file__)) + '/config/soh_sdi.yaml'.replace('/', path.sep))


if __name__ == '__main__':
    main()
