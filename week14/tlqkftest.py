import pyrebase
import json

with open("auth.json") as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

info = {"name":"신하란", "number":"01012345678"}
db.child("정보").child("haran").set(info)

# 일반텍스트로 데이터 집어 넣기!!
info = ["010-1234-1234", "부산광역시"]
db.child("AddressBook2").set(info)
