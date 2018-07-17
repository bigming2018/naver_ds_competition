# 모두를 위한 파이썬

===========================================

## Chapter 06


### 문자열을 다루는 다양한 방법들
- 파이썬 문자열 타입의 내장 메소드


### 문자열 슬라이싱
- 특정 범위에 있는 문자를 가져올 수 있다.

```
myString = 'Monty Python'
print(myString[0:4])  # Mont가 출력. 여기서 0 to 4에 대한 인덱스는 출력되는 값에 포함되지 않는 것을 확인
print(myString[6:7])  # P가 출력
print(myString[6:20]) # Python이 출력
print(myString[:2])   # index 값이 2에 해당하는 문자 앞부터 출력
print(myString[8:])   # index 값이 8에 해당하는 문자부터 출력
print(myString[:])    # 전체가 출력
```


### 문자열 합치기
- 문자열 연결은 수리 연산자인 "+"를 이용해서 달성할 수 있음

```
firstString = 'Hello'
secondString = 'There'
print(firstString + secondString)

thirdString = firstString + '' + secondString
print(thirdString)
```


### in 을 논리 연산자로 사용하기
- 특정 문자열에 우리가 확인하고자 하는 문자가 있는지 확인하기 위해 in 을 사용할 수 있음

```
fruit = 'banana'
print('n' in fruit)     # True로 출력됨
print('m' in fruit)     # False로 출력됨
print('nan' in fruit)   # True로 출력됨

if 'a' in fruit:
    print('Found it!')  # Found it 으로 출력됨
```


### 문자열 라이브러리
- 문자열 타입의 객체에서 다양한 메소드를 사용할 수 있음

```
greet = 'Hello Bob'
zap = greet.lower()
print(zap)                 # hello bob 으로 출력됨
print(greet)               # Hello Bob 으로 출력됨
print('Hi There'.lower())  # hi there로 출력됨
print(greet.upper())       # HELLO BOB으로 출력됨
```


### Strip 메소드
- 문자열에서 공백을 제거하는 메소드
- lstrip() : 왼쪽 공백 제거
- rstrip() : 오른쪽 공백 제거
- strip()  : 오른쪽 왼쪽 공백 제거

```
greet = '           Hello Steven         '
greet.lstrip()      # 왼쪽의 공백이 삭제됨
greet.rstrip()      # 오른쪽의 공백이 삭제됨
greet.strip()       # 양쪽의 공백이 삭제됨
```


### 시작문자열 찾기
- startswith 라는 메소드를 통해서 특정 문자로 문자열이 시작되는지 확인할 수 있음
- 결과값은 불리언 타입으로 반환됨
- 해당 문자로 시작한다면 True, 그렇지 않다면 False가 반환됨

```
line = 'Please hava a nice day'
print(line.startswith('Please')) # True
print(line.startswith('p'))      # False : 대소문자 구분
```
