
# rad: 반지름
# move : 이동거리
import turtle
t = turtle.Turtle() #거북이를 만든다.
t.shape("turtle") #거북이 모양의 그래픽을 사용.
t.width(3) #거북이가 그리는 선의 두꼐를 3으로 한다.

t.shapesize(3, 3) # 거북이를 3배 확대한다.


def turtleMoveLeft(rad, move):
    t.left(rad) #거북이 머리방향에서 왼쪽으로 회전
    t.forward(move)#거북이 머리방향으로 이동.

def turtleMoveRight(rad, move):
    t.right(rad) #거북이 머리 방향에서 오른쪽으로 회전
    t.forward(move)#거북이 머리방향으로 이동.

while True:
    command = input("명령을 입력하시오(i, r, q중) =")
    if command =="i": #사용자가 "I"을 입력하였으면
        turtleMoveLeft(90, 100)
    if command =="r": #사용자가 "r"을 입력하였으면
        turtleMoveRight(90, 100)
    if command == "q": #사용자가 "q"을 입력하였으면
        break #무한 루프를 빠져나간다.

turtle.mainloop()
turtle.bye()