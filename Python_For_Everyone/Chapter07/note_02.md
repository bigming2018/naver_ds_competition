# 모두를 위한 파이썬

===========================================

## Chapter 07


### 파일 읽기
- 읽어들인 파일은 다양한 방식으로 활용할 수 있음


### 파일 핸들
- 파일 핸들(File Handle)은 순서가 있고 연속적으로 구성된 텍스트 파일을 한줄한줄 읽어나가게됨

```
fhand = open('Hamlet.txt')

for line in fhand:
    print(line)
```


### 파일의 라인 수 세기
- 파일의 문장이 몇 줄이 있는지 확인하기 위해서 매우 간단한 방법으로 해결 가능함
```
fhand = open('Hamlet.txt')
count = 0

for line in fhand:
    count = count + 1

print('Line Count:', count)
```


### 파일 전체 읽기
- 전체 텍스트 파일을 단일한 하나의 문장으로 읽어들어올 수 있음
- 각 문장에 대한 구분은 개행문자로 구분되어 있음

```
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])
```


### 파일 내용 검색하기
- 문자열과 관련된 내장 함수를 활용해서 특정 문자열로 시작하는 문자를 찾을 수 있음

```
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
    print(line)

 결과값으로 From: 으로 시작되는 문자열이 출력되게 됩니다.
```

- 하지만 결과를 보면 한 줄씩 띄워져 있는 것을 발견할 수 있음
- print() 함수로 출력되면서 개행 문자가 계속해서 추가되기 때문임
- 새로운 라인은 공백으로 인식되기 때문에 해당 부분을 제거하게 되면
- 기본적으로 추가 되어 있던 개행 문자를 삭제할 수 있다

```
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # 오른쪽 공백 제거
    if line.startswith('From:'):
        print(line)
```


### 파일 이름 입력 받기
- 사용자가 파일의 이름을 직접 입력해야 하는 경우도 있음
- 파일명을 적절히 입력한다면 문제가 없음. 잘못된 파일명을 입력헀을 때 처리방법을 생각해볼 필요가 있음
- try, except 문을 활용해 발생할 수 있는 오류 상황을 적절하게 해결할 수 있음

```
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:')
    count = count + 1
print('There were',count,'subject lines in',fname)
```