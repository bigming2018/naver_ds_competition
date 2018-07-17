### 함수 만들기
- 우리만의 함수 만들기
- 함수를 저장하기 위해서는 def 라는 예약어를 사용

```
def greeting():
    print("Hello World")
```

- :(콜론) 뒤에 실행하고자하는 실행코드를 입력하는 것으로 원하는 결과("Hello World" 출력)를 기대할 수 없음
- 여기까지는 함수 정의 단계
- 원하는 결과, 즉 Hello World가 실행되기를 바라면 사용자가 정의한 이름으로 저장된 함수를 호출해야함
- 여기서는 greeting()이라는 이름으로 호출

```
def greeting():
    print("Hello World")

greeting()
```


### 인자(Argument)
- 인자란 함수를 호출할 때 전달하는 값을 말한다
- 넘겨받는 수 또는 값
- print 함수에 들어가는 문자열도 인자


### 매개변수(Parameters)
- 매개변수는 함수가 정의된 곳에서 변수처럼 사용하는 것

```
def greeting(lang):
    print(lang)

greeting("Hello World")
```


### 반환값(Return Value)
- 종종 함수는 함수가 정의된 곳에서 전달받은 매개변수를 이용해 프로그래머가 의도한 코드를 실행한 뒤
- 계산 결과인 값을 반환할 수도 있음
- 이와 같은 상황에서는 함수를 다른 함수의 인자로 사용할 수도 있음

```
def greeting():
    return "Hello"

print(greet(), "Connect")
print(greet(), "Python")
```


### Multiple 매개변수 / 인자
- 여러개의 매개변수를 받는 함수를 만들 수도 있음
- ex) 더하기 함수

```
def add(left, right):
    return left + right

print(add(1,2))
```