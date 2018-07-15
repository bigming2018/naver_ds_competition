# 모두를 위한 파이썬

===========================================

## Chapter 03

### 조건문(if else)

- 조건부 실행 (Conditional Execution)

### if문
- if 문의 기본적인 형태는 아래와 같다.

```
x = 5

if x < 10:              # if는 예약어이며 컴퓨터는 if 다음에 나오는 조건문의 True, False를 판단하게 된다.
    print('Smaller')    # 만약 True인 경우 :(콜론) 아래로 들여쓰기된 부분을 실행하게됨
```


### 비교연산자
```
x > y : x가 y보다 클 때 true
x < y : x가 y보다 작을 때 true
x >= y : x가 y보다 크거나 같을 때 true
x <= y : x가 y보다 작거나 같을 때 true
x == y : x와 y가 같을 때 true
x != y : x와 y가 다를 때 true
```

### 들여쓰기 (indentation)
- 파이썬에서는 들여쓰기를 매우 엄격하게 생각함
- 들여쓰기가 제대로 되어 있지 않다면 파이썬에서는 문법 에러가 발생함
- 통샹 들여쓰기는 [tab] 또는 [Space] 네 번과 같다.

```
x = 5

if x < 10:
print('Smaller') # 들여쓰기가 되어 있지 않아서 문법 에러 발생함
```

### 조건문을 사용할 시 주의할 점
- 1. 조건문 후에 :(콜론)을 찍는다.
- 2. 조건문이 참일 경우 실행할 코드는 들여쓰기를 한다.


### 조건문(elif)과 예외처리(try, except)
- 다중 분기(Multi-way decision)
- 하나의 조건문 블럭에 프로그래머의 필요에 의해 조건문들을 추가할 수 있음
- elif 라는 예약어를 통해서 가능함

```
x = 21

if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else :
    print('Ginormous')
```

### try / except
- 파이썬에서는 발생할 수 있는 error에 대해 프로그래머가 미리 대처할 수 있도록 함
- try / except 를 이용
- 예를 들어 사용자가 입력값으로 숫자만 넣어야 하는 경우 문자를 넣었을 때
- 프로그램이 종료되고 멈출 것이 아니라 올바른 입력값을 넣도록 하는 것이 합리적임