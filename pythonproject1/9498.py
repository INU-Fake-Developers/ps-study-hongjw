print('시험 점수 입력:') # 시험 점수는 0이상 100이하의 정수
a=int(input('시험 점수 :'))

if 100 >= a >= 90:
    print('A')

elif 89 >= a >= 80:
    print('B')

elif 79 >= a >= 70:
    print('C')

elif 69 >= a >= 60:
    print('D')

else :
    print('F')