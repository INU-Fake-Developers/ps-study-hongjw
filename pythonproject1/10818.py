int(input())          # 정수의 갯수 입력
num =list(map(int,input().split()))  # map= list에 존재하는 항목마다 함수를 적용!
print(min(num),max(num))  # min, max 함수 사용하려면 list화 해야함
