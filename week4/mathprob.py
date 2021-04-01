#산술 문제 출제 프로그램
#while 문을 사용하여 문제 출제를 5번 계속할 수 있도록 수정하시오.
#1문제를 맞추면 10점씩 증가한다. 5번 (마지막)수행 후, 최종 점수와 회수를 출력하시오(점수, 횟수 변수 사용)
#소스 코드의 f-string을 format함수로 바꾸시오.
import random

score = 0
i=0
while i<5: #while반목문을 써서 5번 반복함.
    x = random.randint(1,100) #x에 1~100 임의의 수를 저장.
    y = random.randint(1,100) #y에 1~100 임의의 수를 저장.
    answer = int(input("{} + {} = ".format(x, y))) #format함수를 이용하여 값을 answer 변수에 저장.
    if answer == (x+y): #만약 answer값이 맞다면
        score = score + 10 #스코어 10점 추가.
        print('정답입니다.')
        print("다섯번 반복 후에 당신의 점수가 나타납니다!")
    else:
        print("오답입니다.")
    i+=1

print("당신의 점수는 {}".format(score))

#메모=============================================
#score+=10와 score = score+10은 같다.
#f-string함수
#answer = int(input(f"{x} + {y} ="))
# f-문자열을 사용하였다. 변수를 { }로 감싸서 문자열 안에 넣을 수 있다.
# 앞에 f를 붙인다.
