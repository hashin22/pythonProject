# firbase DB : AddressBook2
from tkinter import *
import pyrebase
import json

window = Tk()
window.title("친구관리")

# Firebase SDK 연결 환경설정 스크립트
with open("auth.json") as f:
    config = json.load(f)

# firebase 초기화
firebase = pyrebase.initialize_app(config)
# db create
db = firebase.database()


def run():
    address_book = {}  # 공백 딕셔너리를 생성한다.
    info = {"name": "신하란", "number": "01012345678"}
    db.child("정보").set(info)
    print("final load", address_book)

def search() :  # 검색
    address_book = {}  # 공백 딕셔너리를 생성한다.
    e1.focus_set()
    t.insert(END, e1.get()+"을 검색하였습니다\n"
             +"\n이름:" + e1.get()
             +"\n 전화번호:" + e2.get()
             +"\n주소:"+ e3.get())
    # 모든 사람 검색 : Dictionary로 출력
    users = db.child("AddressBook2").get(t)
    print(users.val())
    all_users = db.child("AddressBook2").get(t)
    # 모든 사람 검색
    for users in all_users.each():
        print(users.val(t))
        print(users.key(t))
    print("final load", address_book)

def add():  # 추가
    address_book = {}  # 공백 딕셔너리를 생성한다.
    e1.focus_set()
    print("추가")
    # DB에 저장
    t.insert(END, e1.get() + "을 추가 했습니다\n")
    db.child("하란AddressBook").child("name").set(e1.get())
    db.child("하란AddressBook").child("PhoneNumber").set(e2.get())
    db.child("하란AddressBook").child("address").set(e3.get())

def delete():  # 삭제
    e1.focus_set()
    print("삭제")
    t.insert(END, e1.get() + "을 삭제 했습니다\n")
    db.child("하란AddressBook").child("name").remove()
    db.child("하란AddressBook").child("PhoneNumber").remove()
    db.child("하란AddressBook").child("address").remove()


def output():  # 출력
    e1.focus_set()
    print("출력")
    t.insert(END, "이름:" + e1.get()
             + "\n 전화번호:" + e2.get()
             + "\n주소:" + e3.get()
             +"을 출력했습니다.")

def saveExit():  #종료
    print("저장 & 종료")
    t.insert(END, "저장 & 종료\n")
    exit()






# Label 객체 생성 및 배치
l1 = Label(window, text="이름", pady=5)
l1.grid(row=0, column=0, sticky=W)
l2 = Label(window, text="전화번호")
l2.grid(row=1, column=0, sticky=W, pady=5)
l3 = Label(window, text="주소")
l3.grid(row=2, column=0, sticky=W, pady=5)
# Entry 객체 생성 및 배치
e1 = Entry(window, bg="orange", width=26)
e2 = Entry(window, bg="orange", width=26)
e3 = Entry(window, bg="orange", width=26)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
# Button 들을 배치하기 위한 Frame 생성 및 배치, window가 부모임
bFrame = Frame(window, pady=5)
bFrame.grid(row=3, column=0, columnspan=2)
b1 = Button(bFrame, text='검색', width=6, command=search)
b1.grid(row=0, column=0, padx=2)
b2 = Button(bFrame, text='추가', width=6, command=add)
b2.grid(row=0, column=1, padx=2)
b3 = Button(bFrame, text='삭제', width=6, command=delete)
b3.grid(row=0, column=2, padx=2)
b4 = Button(bFrame, text='출력', width=6, command=output)
b4.grid(row=0, column=3, padx=2)
b5 = Button(bFrame, text='종료', width=6, command=saveExit)
b5.grid(row=0, column=4, padx=2)
# Text 객체 생성 및 배치
t = Listbox(window, bg="orange", height=12, width=50, border=0)
t.grid(row=4, column=0, columnspan=2, pady=2)
# Create scrollbar
scrollbar = Scrollbar(window, orient='vertical')
scrollbar.grid(row=4, column=2, sticky=N+S)
# Set scroll to listbox
t.configure(yscrollcommand=scrollbar.set)
# scrollbar 실행
scrollbar.configure(command=t.yview)
# __main__은 프로그램의 시작점
if __name__ == '__main__':
    run()

window.mainloop()