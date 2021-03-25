def Calculrator(z):
    x = int(input("첫번째 숫자를 입력하세요. ")) #x에 숫자를 저장함
    y = int(input("두번째 숫자를 입력하세요. ")) #y에 숫자를 저장함
    if z == 1: # 처음 1을 입력 받으면 더하기 함수를 호출하여 값을 밖으로 보냄
        return plus(x,y)
    elif z == 2: # 마찬가지로 2를 입력 받으면 빼기 함수를 호출하여 값을 밖으로 보냄
        return minus(x,y)
    elif z == 3: # 곱하기 함수를 호출하여 값을 밖으로 보냄
        return mul(x,y)
    elif z == 4: # 나누기 함수를 호출하여 값을 밖으로 보냄
        return div(x,y)
    else: # 나머지 함수를 호출하여 값을 밖으로 보냄
        return rem(x,y)

def plus(a,b): #더하기 함수
    return a,b
def minus(a,b): #빼기 함수
    return a-b
def mul(a,b): #곱하기 함수
    return a*b
def div(a,b): #나누기 함수
    return a//b #정수만 출력.
def rem(a,b): # 나머지 함수
    return a%b

print("====================================")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")
print("5.나머지구하기")
print("6.나가기")
print("====================================")

while True:
    ans = int(input("1, 2, 3, 4, 5, 6중 숫자를 입력해주세요 ")) #ans에 숫자를 저장함
    if ans == 6: break #나가기 숫자 6을 입력하면 while문을 빠져나오고 프로그램이 종료
    print("결과는",Calculrator(ans),"입니다.")