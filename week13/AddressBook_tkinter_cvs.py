from tkinter import *
import json
window = Tk()
window.title("친구관리")

address_book = {}  # 공백 딕셔너리를 생성한다.
def add() :
    name = e1.get()
    phone = e2.get()
    address = e3.get()
    print(name)
    info = [phone, address]
    print(address_book)
    print("추가")
    t.insert(END, "이름:" +name+ "을 추가 했습니다"+"\n")
    t.insert(END, "전화번호:" +info[0]+ "을 추가 했습니다"+"\n")
    t.insert(END, "주소:" +info[1]+ "을 추가 했습니다"+"\n")
    e1.focus_set()


def delete() :
    key = e1.get()
    print(type(key))
    print(type(address_book.get(key)))
    print(address_book)

    if address_book.get(key) is None:
        t.insert(END, "저장되지않은 이름입니다.")
    else:
        address_book.get(key)
        t.insert(END, key + "님이 삭제되었습니다.\n")
        e1.delete(0, END)
        e1.focus_set()


def search() :
    key = e1.get()
    print(type(key))
    print(type(address_book.get(key)))
    print(address_book)

    if address_book.get(key) is None:
        t.insert(END, "저장되지않은 이름입니다.")
    else:
        info = address_book.get(key)
        t.insert(END, key + "을 검색 했습니다\n")
        t.insert(END, info[0] + "을 검색 했습니다\n")
        t.insert(END, info[1] + "을 검색 했습니다\n")
        e1.delete(0, END)
        e1.focus_set()

def output() :
    e1.focus_set()
    print("출력")
    t.insert(END, e1.get() + "을 출력 했습니다\n")
    e1.delete(0, END)

def saveExit() :
    addressData = {'홍길동': '010-1234-1234', '이순신': '010-2222-2222'}
    # 파일저장
    with open('./addressData.json', 'w', encoding='utf-8-sig') as f:
        json.dump(addressData.json, f, ensure_ascii=False, indent=4)
    f.close()
    print("저장 & 종료")
    t.insert(END, "저장 & 종료\n")
    exit()

address_book = {}  # 공백 딕셔너리를 생성한다.
def fileLaod():
    global address_book
    try:
        with open('./addressData.json', 'r', encoding='utf-8-sig') as f:
            lines = json.load(f)
            print(lines)
            address_book = lines
            print("final END", address_book)
            address_book = json.reader(f)  # csv파일을 address에 저장

    except FileNotFoundError as e:
        print('파일이 존재하지 않습니다..', e)

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
t = Listbox(window, bg="orange", height=12, width=33, border=0)
t.grid(row=4, column=0, columnspan=2, pady=2)

# Create scrollbar
scrollbar = Scrollbar(window, orient='vertical')
scrollbar.grid(row=4, column=2, sticky=N+S)
# Set scroll to listbox
t.configure(yscrollcommand=scrollbar.set)
# scrollbar 실행
scrollbar.configure(command=t.yview)
# Bind select
# t.bind('<<ListboxSelect>>', select_item)

window.mainloop()