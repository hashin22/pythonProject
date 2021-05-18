# data.txt
# 홍길동,010-1234-5678,부산시 양정동 동의과학대학교
# 박찬호,서울시 영등포구,010-22132-12321
# 박세리,충청북도 청원군,010-1111-111
# 이순신,010-9999-999,충청남도 아산
# 강감찬,010-8888-8888,충청북도 청원군
# 손홍민,010-1234-5678,프리미어 리그

# 빈 딕셔너리 생성
address_book = {}

with open("./data.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        # print(line)
        # 추후 처리를 위하여 딕셔너리에 넣기
        # split로 문자열을 분리하여 리스트에 저장
        raw = line.split(',')
        # print(raw[0])
        key = raw[0]  # name
        vals = [raw[1], raw[2].rstrip()] # list[phone_no, addreaa)
        print(key, vals)
        # 딕셔너리의 데이터 저장
        address_book[key] = vals
        
    # print(address_book)

# 딕셔너리의 데이터 추가
address_book["손홍민"] = ["010-1234-5678", "프리미어 리그"]
print(address_book)

# 딕셔너리 삭제
address_book.pop("임꺽정")
print(address_book)

# 딕셔너리 저장
with open("./outData.txt", "w") as f:
    for key in address_book:
        f.write(key + ',')
        f.write(address_book[key][0] + ',')
        f.write(address_book[key][1] + '\n')
    f.close()
