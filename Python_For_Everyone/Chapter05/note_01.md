# 모두를 위한 파이썬

===========================================

## Chapter 05


### 들어가기
- 컴퓨터가 인간보다 나은 점은 하나의 작업을 반복적으로 빠르게 수행할 수 있다는 것
- 이를 루프라고 한다.


### while 루프

- while과 : (콜론) 사이에 오는 조건문이 참의 값을 가지는 경우에는 :(콜론) 이하의 코드가 반복해서 작동함
- while 은 반복적으로 작업할 수 있도록 해주는 편리한 문법
- 무한루프에 빠질 수 있다는 단점도 내포한다

```
n = 5

while n > 0:
    print(n)
    n = n - 1

print('Blastoff!')
print(n)
```


### 루프(Loop) 제어하기
### break
- 루프가 break를 만나면 해당 루프는 실행이 종료되고 while 문 바로 뒤의 코드를 실행한다

```
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')
```


### continue
- 루프가 continue를 만나게 되면 해당 루프는 실행이 종료되고 루프가 시작된 지점부터 다시 루프를 실행하게 된다.

```
while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
```


### for 루프
- 유한개의 항목을 가지고 있고 인간의 의도적 행위 없이 주어진 항목들을 모두 순회하게 되면 종료되는 루프
- 하나의 파일에 들어 있는 문장의 갯수와 리스트 안에 들어 있는 항목들의 수는 유한개이다.
- 유한개의 항목들에 대해 특정 조치들을 취하고 싶을 때 for 루프를 사용

```
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
```

- 문자열 리스트에서도 동일한 방식으로 출력 가능함

 ```
 friends = ['Yun Young', 'Lim seul ki', 'Kim min su']
 for friend in friends:
    print('Happy Birth Day!',friend)
 print('Done!)'
 ```