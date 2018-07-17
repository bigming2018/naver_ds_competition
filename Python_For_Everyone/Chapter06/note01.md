# 모두를 위한 파이썬

===========================================

## Chapter 06


### 문자열
- 데이터는 다양한 타입으로 저장됨
- 특히 문자열은 많이 사용하게됨
- 문자열 타입과 관련하여서는 타입 변환, 인덱싱, len 함수, for 루프 활용을 이해하고 사용할 수 있어야함


### 문자열 읽기, 타입 변환
- 문자열을 사용한 데이터를 읽어 오게 되면 에러나 사용자 입력에 대해 많은 대처를 할 수 있음
- 사용자 입력으로 들어오는 값은 문자열 타입으로 입력됨
- 입력된 값으로 다른 무엇인가를 하기 원한다면 적절한 타입 변환이 필요함

```
name = input('Enter:')
print(type(name))
print(name)

# > Enter: 123으로 입력함
# 인풋값 123의 타입은 <class 'str'> 과 같다
# 123으로 출력됨
```


### 문자열 내부 들여다 보기
- 특정 문자열을 구성하고 있는 개별 문자 값에 인덱스를 활용하여 접근할 수 있음
- 첫번째 오는 문자에 대한 인덱스는 0부터 시작한다
- 만약 해당 문자열이 가지고 있는 인덱스를 넘어서는 값을 호출하게 되면 오류가 발생함

```
fruit = 'banana'
letter = fruit[0]
print(letter)

letter = fruit[1]
print(letter)

letter = fruit[2]
print(letter)
```


### len 함수
- 문자열에 대해서 len() 내장 함수를 활용해서 문자열의 길이를 알 수 있음
- 예를 들어 len(banana) 라고 한다면 banana 가 몇 개의 문자로 구성되어 있는지를 알 수 있음

```
fruit = 'banana'
print(len(fruit))
```


### 문자열의 길이만큼 루프 실행
- len() 함수를 활용하면 문자열의 길이만큼 루프를 실행할 수 있음

```
fruit = 'banana'
index = 0

while index < len(fruit)
    letter = fruit[index]
    print(index, letter)
    index = index + 1


for letter in fruit
    print(letter)
```