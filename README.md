#1 venv환경 만들기
app 부모 폴더에서
$virtualenv venv
venv 세팅 후
$ source venv/bin/activate

#2 패키지 설치
app 폴더에서 
$ pip3 install requirement.txt

#3 실행
app 폴더에서 
$ uvicorn main:app
