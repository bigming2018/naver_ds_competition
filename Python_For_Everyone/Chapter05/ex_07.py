# 반복문 응용
# 루프를 사용하여 평균 구하기

# 원소의 수와 총합을 활용하면 평균을 구할 수 있다

count = 0 # 평균을 전체 원소의 수로 나누기 위해 total number 를 확인
sum = 0
print('Before',count,sum)

numbers = [9,41,12,3,74,15]

for value in numbers:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)