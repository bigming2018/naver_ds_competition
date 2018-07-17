fruit = 'apple'
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1



for letter in fruit:
    print(letter)



myString = 'Monty Python'
print(myString[0:4])
print(myString[6:7])
print(myString[6:20])
print(myString[:2])
print(myString[8:])
print(myString[:])


# 문자열 합치기
# 문자열 연결은 수리 연산자인 "+"를 이용
firstString = 'Hello'
secondString = 'Python'
print(firstString + secondString)

thirdString = firstString + ' ' + secondString
print(thirdString)


# in 을 논리 연산자로 사용하기
# 특정 문자열에 확인하고자 하는 문자가 있는지 확인하기 위해 in 을 사용
fruit = '윤영'
print('윤' in fruit)
print('a' in fruit)
print('nan' in fruit)

if 'a' in fruit:
    print('Found it!')


# 문자열 라이브러리
greet = 'Hello Kaita'
zap = greet.lower()
print(zap)
print(greet)
print('Hi Pychorn'.lower())
print(greet.upper())



# Strip 메소드 (문자열에서 공백 제거)
# lstrip() : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백 제거
# stript() : 오른쪽 왼쪽 공백 제거

greet2 = '         Welcom to Korea!          '

print(greet2)
print(greet2.lstrip())
print(greet2.rstrip())
print(greet2.strip())


### 시작 문자열 찾기 : startswith
line = 'Have a nice day!'
print(line.startswith('Have'))
print(line.startswith('H'))
print(line.startswith('h'))