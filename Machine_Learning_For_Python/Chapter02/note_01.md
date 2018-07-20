# 머신러닝을 위한 Pyyhon

===========================================

### Pythonic Code Overview

- 파이썬 스타일 코드(Pythonic Code)
- Pythonic Code 는 간단하게, 다른 사람의 코드를 잘 이해하기 위해서
- 파이썬 특유의 문법을 활용하여 효율적으로 코드를 표현하는 기법을 말함


### Why Pythonic Code?
- 남 코드에 대한 이해도
- 많은 개발자들이 python 스타일로 코딩한다
- 효율
- 단순 for loop append 보다 list가 조금 더 빠르다
- 익숙해지면 코드도 짧아진다
- 간지
- 쓰면 왠지 코드 잘 짜는 것처럼 보인다


### 일반 코드

```
colors = ["red", "blue", "green", "yellow"]
result = ""

for s in colors:
    result += s

print(result)
```


### pythonic code
```
colors = ["red", "blue", "green", "yellow"]
result = "".join(colors)

print(result)
```