#연습문제 11번

# 체 질량지수(BMI) 판별
# 체질량지수 = 체중/키의제곱(m)
# 정상 : 18.5 ~ 24.9
# 과체중 : 24.5 ~ 29.9
# 비만 : 30.0 이상
while True:
    weight = float(input('무게를 입력하세요 Kg (0은 종료)')) #float로 무게를 실수로 반환합니다.
    if weight==0:                                       #만약 몸무게 값을 0으로 입력했을 때
        break                                           #종료
    if weight < 0:                                      #만약 몸무게 값이 0보다 작을 때
        print('올바른 값이 아닙니다.')                      #올바른 값이 아니라고 출력.
        continue                                        # 반복문의 처음으로 갑니다.

    height = float(input('신장을 입력하세요(0은 종료)')) #float로 키를 실수로 반환합니다.
    if height==0:                                   #만약 신장의 값을 0으로 입력했을 때
        break                                       #종료합니다.
    if height < 0:                                  #만약 신장의 값을 0보다 작게 입력했을 때
        print('올바른 값이 아닙니다.')                  #올바른 값이 아니라고 출력합니다.
        continue                                    #반복문의 처음으로 갑니다.

    bmi = weight/(height/100)**2 #BMI 구하는 식 = 체중/(신장)^2

    if bmi<18.5:            #BMI가 18.5q보다 작을 때
        print('BMI 값이 {:.2f}이므로 "저체중"입니다.'.format(bmi)) #'{인덱스0}, {인덱스1}'.format(값0, 값1)
    elif bmi >= 18.5 and bmi <=24.9:
        print('BMI 값이 {:.2f}이므로 "정상"입니다.'.format(bmi)) #{:.2f} -> 소수점 둘째자리까지만 표현
    elif bmi >= 24.5 and bmi <= 29.9:
        print('BMI 값이 {:.2f}이므로 "과체중"입니다.'.format(bmi))
    else:
        print('BMI 값이 {:.2f}이므로 "비만"입니다.'.format(bmi))

    result = '비만'
    if 20 <= bmi <= 24.9:
        result = '정상'
    elif 25 <= bmi <= 29.9:
        result = '과체중'
    else:
        result = '비만'

    print('BMI 값이 {0:.2f}이므로 "{1}"입니다.'.format(bmi, result)) #'{인덱스0}, {인덱스1}'.format(값0, 값1)
                                                                  # {:.2f} -> 소수점 둘째자리까지만 표현
    result = '비만'
    if bmi < 18.5:
        result = '저체중'
    elif bmi <= 24.9:
        result = '정상'
    elif bmi <= 29.9:
        result = '과체중'

    print('BMI 값이 {0:.2f}이므로 "{1}"입니다.'.format(bmi, result))