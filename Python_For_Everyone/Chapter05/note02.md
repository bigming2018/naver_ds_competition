### 반복문

### 루프의 응용
- 특정 조건이 참인 경우에는 반복적으로 실행되는 불확정 루프의 종류인 while문
- 유한 개의 요소를 가지고 있으며 개별 요소를 모두 순회하게 되면 종료되는 for 루프

- 예시 : for 루프를 이용해 가장 큰 수를 찾아내는 코드

```
largest_so_far = -1
print('Before', largest_so_far)
numbers = [9, 41, 12, 3, 74, 15]
for the_num in numbers:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print('largest_so_far:', largest_so_far, 'current number:', the_num)
print('After',largest_so_far)
```

- 가장 큰 수를 찾는 문제에 대해서 인간이 해결하는 방식과 컴퓨터가 해결하는 방식이 차이가 있음
- 인간은 전체의 수가 펼쳐져 있는 상태에서 가장 큰 수를 찾기 위해 앞뒤로 유동적으로 비교하는 반면
- 컴퓨터는 순차적으로 인간이 입력한 코드에 따라 숫자를 비교함


### 반복문 응용

### 들어가기
- 루프를 활용해 몇 가지 패턴을 알게되면 다양한 작업들을 수행할 수 있음
- 가장 큰 수를 찾거나, 리스트의 원소의 수를 계산하는 등 사람이 하기에는 귀찮은 작업들을 컴퓨터는 빠르게 처리함


