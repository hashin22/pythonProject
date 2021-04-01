#연습문제 3번

var = input("문자를 입력하세요 =") #문자를 var이라는 변수에 입력 받음.

if(var == 'R'): #문자가 R이면
    print("Rectangle") #Rectangle 이라고 출력한다.
elif(var == 'T'): #문자가 R이면
        print("Triangle\n") #Triangle 이라고 출력한다.
elif(var == 'C'): #문자가 R이면
        print("Circle\n") #Circle 이라고 출력한다.
else: #그 외의 문자가 들어오면
    print("Unkown\n") #unkown 이라고 출력한다.
