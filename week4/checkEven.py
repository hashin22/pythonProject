#p.126


def checkEven0dd(n):
    if n % 2 ==0: #n을 2로 나눴을때 0이라면
        return "짝수" #짝수로 출력을 한다.
    else: #그 외의 숫자를 입력받으면
        return "홀수" #홀수로 출력을 한다.

while True:
    number = int(input("정수를 입력하시오 =")) #number이란 변수에 정수를 입력받는다.
    if number != 0000: #0000이 아니라면 함수 checkEven0dd를 실행한다.
         print(f'{number}는',checkEven0dd(number))
         # format함수
         # print('{0}은 {1}입니다'.format(number, checkEven0dd(number)))
    else: # 그외라면
        print('bye bye') #종료하도록 한다.
        break


    # 다른 코드==================
    # if number == 0000:
    #     print('bye bye')
    #     break
    # else:
    #     result = checkEven0dd(number)
