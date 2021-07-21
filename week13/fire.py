import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCgO1DdVpFWZFwxuUIRnI9UVr2hS3Fetxw",
    "authDomain": "webtest-4e160.firebaseapp.com",
    "projectId": "webtest-4e160",
    "storageBucket": "webtest-4e160.appspot.com",
    "messagingSenderId": "815305867386",
    "appId": "1:815305867386:web:02118f093666251bfdbbc3",
    "measurementId" : "G-TRVS2GQNTZ"
  };

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
info=["010-1234-1234", "부산시 민락동"]

# key 생성
db.child("AddressBook2").child("신하란").set(info)
db.child("test").push("010-1234-5678")

# push : key가 자동생성
db = firebase.database()
data = {"name":"신하란"}
db.child("users").push(data)
print("Data updated successfully")

# set : 명시적인 key 사용
db.child("users").child("name").set(data)

#update
db.child("users").child("name").update({"name": "도경수"})
print("DAta updated successfully")

# query: Object전체 값 읽기
users = db.child("AddressBook").get()
print(users.val())

# 개별 key(), val() 읽기
all_users = db.child("AddressBook").get()
for user in all_users.each():
    print(user.key())
    print(user.val())