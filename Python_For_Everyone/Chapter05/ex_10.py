# 반복문 응용

# 가장 작은 수를 찾는 코드 완성하기
# None 자료형 : None은 값이 없다는 것을 말함.
# 하나의 빈 상자에 이 상자는 비어있습니다 라고 명시적으로 표시

# "is", "is not" 연산자는 자료형과 값이 동일할 때 True를 반환함
# 0 == 0.0 은 True
# 0 is 0.0 은 False (값은 동일하지만 자료형이 전자는 int 이고 후자는 float이기 때문에 False)

smallest = None
print('Before')

numbers = [9,41,12,3,74,15]

for value in numbers:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After',smallest)