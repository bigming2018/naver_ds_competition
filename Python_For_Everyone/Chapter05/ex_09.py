# 반복문 응용
# 부울값을 사용하여 특정 값을 검색하기

# 원하는 특정 값이 list 에 있는지 확인
# 부울 변수 이용

found = False
print('Before', found)

numbers = [9, 41, 12, 3, 74, 15]

for value in numbers:
    if value == 3:
        found = True
        print(found, value)
        break
print('After', found)