#5번
# 3개의 정수 입력받아서 if-else문을 사용하여 가장 작은 값을 결정하는 문.

a=int(input('첫번 째 수 = ')) #input함수를 호출하여 입력된 값을 변수 a에 저장합니다.
b=int(input('두번 째 수 = ')) #input함수를 호출하여 입력된 값을 변수 b에 저장합니다.
c=int(input('세번 째 수 = ')) #input함수를 호출하여 입력된 값을 변수 b에 저장합니다.

def myMin(a, b, c):
    if a <= b: #a가 b보다 작거나 같다면
        return a #리턴 값을 a로 줍니다.
    elif b <= c: #b가 c보다 작거나 같다면
        return b #리턴 값을 b로 줍니다.
    elif c <= a: #c가 a보다 작거나 같다면
        return c #리턴 값을 c로 줍니다.

print("제일 작은 수는", myMin(a, b, c)) #myMin함수를 호출하여 입력된 정수 3개중 제일 작은 정수를 구합니다



