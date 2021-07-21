# 참고 문서 : https://bit.ly/3vWoe1P
# databaseURL : https://hello-python-c92f9-default-rtdb.firebaseio.com
import pyrebase

config = {
    "apiKey": "AIzaSyCP37bKQ3ZXQaos0zBipDCmGigMp6AV9Qc",
    "authDomain": "hello-python-c92f9.firebaseapp.com",
    "databaseURL": "https://hello-python-c92f9-default-rtdb.firebaseio.com",
    "projectId": "hello-python-c92f9",
    "storageBucket": "hello-python-c92f9.appspot.com",
    "messagingSenderId": "765437838021",
    "appId": "1:765437838021:web:3781004812462136cda6ac",
    "measurementId": "G-11J6FDPS2Z"
}

# firebase 초기화
firebase = pyrebase.initialize_app(config)

# db create
db = firebase.database()
info = ["010-1234-1234", "부산시 양정동"]
db.child("AddressBook2").child("김종현").set(info)

# update
updateInfo = ["010-7777-7777", "부학대학교"]
db.child("AddressBook2").update({"이순신":updateInfo})

# query

# 모든 사람 검색 : Dictionary로 출력
users = db.child("AddressBook2").get()
print(users.val())

# 특정 사람 검색
users = db.child("AddressBook2").child("홍길동").get()
print(users.val())

all_users = db.child("AddressBook2").get()

# 모든 사람 검색
for users in all_users.each():
    print(users.val())
    print(users.key())

# delete
db.child("AddressBook2").child("김기찬").remove()