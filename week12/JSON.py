import json

def start():
    address_book = {}  # 공백 딕셔너리를 생성한다.

    try:
        with open('./addressData.json', 'w', encoding='utf-8-sig') as f:
            address_book = json.reader(f) #csv파일을 address에 저장
            for line in address_book: #address를 line
                print(line)
            f.close()
            print("파일을 불러왔습니다", address_book)
    except FileNotFoundError as e:
        print('파일이 존재하지 않습니다..', e)

        f = open('./1.csv', 'w', encoding='utf-8')  # 파일 불러오기
    while True:
        user = display_menu()

        if user == 1: # 추가
            f = open('./addressData.json', 'w', encoding='utf-8') #파일 불러오기
            wr = json.writer(f) #파일쓰기 변수 선언
            addressData = {'홍길동': '010-1234-1234', '이순신': '010-2222-2222'}
            obj1 = json.dumps(addressData, ensure_ascii=False)
            print(obj1)  # 문자열(str)로 출력
            print(type(obj1))
            with open('./addressData.json', 'w', encoding='utf-8-sig') as f:
                json.dump(addressData.json, f, ensure_ascii=False, indent=4)


        elif user == 2:  # 삭제
            number = input("삭제할 번호 입력 : ")
            for row in address_book:
                if row[0] != number:
                    wr.writerow(row)
                f.close()
            print(f'{number}  삭제 되었습니다')

        elif user == 3: # 검색
            select = input("검색할 번호 입력 : ")
            if address_book(select) is None:
                print("저장되지 않은 번호입니다.")
            else:
                f = address_book(select)
                print(select, "의 번호 :", f)

        elif user == 4: # 출력
            f = open('./1.csv', 'r', encoding='utf-8')
            rdr = json.reader(f)
            for line in rdr:
                print(line)
            f.close()

        else:  # 파일 저장
            # loads : JSON 문자열(파이썬 객체)을 읽어 딕셔너리에 저장
            dict2 = '{"박찬호": "010-1234-1234", "차범근": "010-4569-2345"}'
            obj2 = json.loads(dict2)
            print(obj2)
            print(type(obj2))
            break

def get_contact():
    number = input("숫자 :")
    name = input("이름 :")
    date = input("날짜 :")
    phone = input("주소 :")
    time = input("시간 :")

    return (number, name, phone, date, time)

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
if __name__ == '__main__':
    start()