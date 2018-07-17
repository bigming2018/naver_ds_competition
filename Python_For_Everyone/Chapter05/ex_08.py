# 반복문 응용

# 루프를 사용하여 필터링 하기
# 특정 값보다 큰 수를 print를 이용해 확인할 수 있다

print('Before')
numbers = [9,41,12,3,74,15]

for value in numbers:
    if value > 20:
        print('Large number', value)
print('After')