import re
infile = open("./input.txt")
addressData={}
while True:
    line = infile.readline()
    if not line:
        break

    print(raw[0])
    print(raw[1], [2])

    raw = line.split(",")
    raw2 = re.sub("\n", "",raw[2])
    #info: value list
    info = [raw[1], raw[2]]
    addressData[raw[0]] = info
print(addressData)


    info = [raw[1], re]
    print(line.strip()) #엔터? 띄어쓰기 없어줌 줄띄어쓰기없애줌
    print(line.strip().rstrip('*').lstrip('*')) #별표표시 없애줌
