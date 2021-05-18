import json

def main():
    address_book = {}  # 공백 딕셔너리를 생성한다.

    try:
        with open('./addressData.json', 'r', encoding='utf-8-sig') as f:
            while True:
                lines = json.load(f)
                print("lines:", lines)
                print(type(lines))
                address_book = lines
                print("final load", address_book)

    except FileNotFoundError as e:
        print('파일이 존재하지 않습니다..', e)

    while True:
        user = display_menu()
        if user == 1:
            name, phone, add = get_contact()
            info = [phone, add]
            # print('name:', info)
            print('info', info)
            # 딕셔너리의 데이터 추가
            address_book[name] = info

        elif user == 2:  # 삭제
            name = input("삭제할 이름 입력 : ")
            address_book.pop(name)
            print(f'{name} 님이 삭제 되었습니다')

        elif user == 3: # 검색
            key = input("검색할 이름 입력 : ")
            if address_book.get(key) is None:
                print("저장되지 않은 이름입니다.")
            else:
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0])
                print(key, "의 주소 :", info[1])
        elif user == 4: # 출력
            for key in sorted(address_book):
                info = address_book.get(key)
                print(key, "의 전화번호 :", info[0], key, "의 주소 :", info[1])

        else:  # 파일 저장
            with open('./addressData.json', 'w', encoding='utf-8-sig') as f:
                json.dump(address_book, f, ensure_ascii=False, indent=4)
            f.close()
            print("파일을 저장하고 종료합니다.")
            break

def get_contact():
    name = input("이름 :")
    phone = input("전화번호 :")
    add = input("주소 :")
    return (name, phone, add)

# 메뉴를 화면에 출력한다.
def display_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

# __main__은 프로그램의 시작점
main()

# 딕셔너리 삭제
# address_book.pop("임꺽정")
# print(address_book)