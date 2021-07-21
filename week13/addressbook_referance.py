# 참고 학습 자료 : https://morioh.com/p/71358deec9e1?f=5c224490c513a556c9042463&fbclid=IwAR11TrgxRq02x6NVVXcbQbKvas8Axjru1SmaW_KFD9zb6Tt9VP9DOGk5r5E
# firbase DB : AddressBook2

import pyrebase

# Firebase SDK 연결 환경설정 스크립트
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

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def run():
    address_book = {}  # 공백 딕셔너리를 생성한다.
    # friend = db.child("AddressBook2").child("김종현").get()
    all_users = db.child("AddressBook2").get()
    for users in all_users.each():
        print(users.val())
        print(users.key())
        address_book[users.key()] = users.val()

    print("final load", address_book)

    while True:
        user = display_menu()
        if user == 1:  # 검색
            key = input("검색할 이름 입력 : ")
            if address_book.get(key) is None:
                print("저장되지 않은 이름입니다.")
            else:
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0])
                print(key, "의 주소 :", info[1])
        elif user == 2:  # 추가
            name, number, add = get_contact()
            info = [number, add]
            address_book[name] = info
            print(name + " 님이 추가 되었습니다.")
            # DB에 저장
            # set은 사용자 key가 있을때, push는 key가 자동으로 생성
            # db.child(name).push(info)
            db.child("AddressBook2").child(name).set(info)
        elif user == 3:  # 수정
            name = input("수정할 이름 입력 : ")
            if address_book.get(name) is None:
                print("저장되지 않은 이름입니다.")
            else:
                # 수정 key, value 출력
                info = address_book.get(name)
                print(name, "의 전화번호 :", info[0], " 주소 :", info[1])

                number = input(("수정할 전화번호는 : "))
                add = input("수정할 주소는 : ")
                db.child("AddressBook2").update({name: [number, add]})
            print("데이터가 성공적으로 수정되었습니다.")
        elif user == 4:  # 삭제
            name = input("삭제할 이름 입력 : ")
            address_book.pop(name)
            print(name + " 님이 삭제 되었습니다")
            # DB에서 삭제
            db.child("AddressBook2").child(name).remove()
        elif user == 5 :  # 출력
            for key in sorted(address_book):
                info = address_book.get(key)
                print(key, "의 전화번호:", info[0], "  주소:", info[1])
        else:  # 종료
            break


def get_contact():
    name = input("이름 : ")
    number = input("전화번호 :")
    add = input("주소 : ")
    return (name, number, add)

# 메뉴를 화면에 출력한다.
def display_menu():
    print("1. 연락처 검색")
    print("2. 연락처 추가")
    print("3. 연락처 수정")
    print("4. 연락처 삭제")
    print("5. 연락처 출력")
    print("6. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

# __main__은 프로그램의 시작점
if __name__ == '__main__':
    run()