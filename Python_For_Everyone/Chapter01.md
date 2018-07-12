# 모두를 위한 파이썬

==================================

## Chapter 01


### Intro

- Python3 설치
- Atom 설치


### 1강. 프로그래밍을 왜 할까?

- 파이썬은 데이터 마이닝, 분석 등을 위한 좋은 프로그래밍 언어
- 프로그램 : 사용자의 요구를 충족시키기 위해 컴퓨터 내에 있는 자원에게 내리는 명령문들의 집합


### 2강. Hardware Architecture

- 하드웨어 구조
- 컴퓨터에서 뇌와 가장 비슷한 기능을 하는 것은 소프트웨어이다
- 하드웨어에서 뇌와 가장 비슷한 기능을 하는 것은 마이크로 프로세서. 
- 중앙연산처리장치(CPU)라고도 함.
- 메인 메모리는 매우 빠름. 하지만 전원을 끄면 정보가 사라짐
- 보조 저장소는 전원이 꺼져도 영구적으로 메모리를 저장함
- 사람이 작성한 파이썬 파일은 CPU가 이해할 수 있는 언어로 번역됨 (0과 1로 이루어진 기계어)

- CPU(Central Processing Unit) : 프로그램을 실행함. 
- CPU는 항상 다음에 무엇을 하지라고 물어본다. 인간의 뇌처럼 지능을 가진 것은 아니고 처리 능력이 매우 뛰어남
- 입력 장치 : 사람에 의해 정보를 입력받는 기기들. 예를 들어 키보드, 마우스, 터치 스크린
- 출력 장치 : 처리된 정보의 결과를 보여주는 기계. 예를 들어 화면, 스피커, 프린터, DVD 기록기
- 메인 메모리 : 적은 양의 정보 를 저장하는 장치이며 속도는 매우 빠르지만 컴퓨터를 종료하면 사라지는 휘발성 메모리
- 보조 기억 장치 : 지우지 않는 이상 정보를 계속해서 가지고 있다. 예를 들면 SDD, HDD가 있다.


### 3강. Python as a Language
- 파이썬은 '파이써니스타'들이 쓰는 언어
- 귀도 반 로섬이 발명한 언어
- 파이썬이 인기가 많은 이유  : 배우기 쉽고 간결하고 강력하기 때문
- 문법 에러(Syntax Errors)

```
python3

x = 1
print(x)

x = x + 1
print(x)

exit()
```

> x=1      : x라는 기억장소에 1을 집어넣으라는 뜻
> print(x) : x라는 기억장소에 저장된 값을 보여주라는 뜻
> x = x+1  : 예전 x값에 1을 더해 x에 넣으라는 뜻
> = : x를 가르키는 화살표와 같은 것임


### 4강. 예악어, 순차문, 조건문 및 반복문
- Elements of Python
- Reserved Words
- You cannot use reserved words as variable names / identifiers

> False		class 	return 		is	     	finally
> None  	if    	for    		lambda  	continue
> True  	def   	from   		while   	nonlocal
> and   	del   	global 		not     	with
> as    	elif  	try    		or      	yield
> assert    else    import      pass    
> break     except  in          raise

- 예약어 (reserve word) : 지정한 의미로만 쓰이는 단어. 지정한 의미가 아닌 다른 의미로는 쓸수 없음. 일종의 약속과 같음

- 파이썬 프로그램은 문장으로 구성되어 있음
- 컴퓨터가 다음으로 원하는 것이 있기 떄문에 순서가 있음

- Sentences or Lines
- +, = 는 연산자
```
x = 2      #변수 x에 상수 2를 넣으라는 명령. x는 사용자가 지정한 변수 이름
x = x + 2  #x에 2를 더한 다음 결과값인 4를 x에 넣으라는 뜻
print(x)   #print(x)는 x에 있는 값을 출력하라는 뜻
```


- Programming Paragraphs
- 프로그램이 길어지면 스크립트로 작성하는 것이 편리함
- 파일에 프로그램을 짜면 파이썬이 코드를 순서대로 읽음
- 파일 이름을 .py로 지정함

- Program Steps or Program Flow
- 순차문 : 순서대로 진행하는 것
- 조건문 : 어느 부분을 건너뛰는 것
- 반복문 : 계속 반복하는 것

- 1. 순차문
- 코드가 처음 줄부터 차례대로 실행되는 경우이다. 짧고 단조로운 코드만 짤 수 있음
```
x = 2
print(x) 	# 2를 출력
x = x + 2 
print(x)  	# 4를 출력
```

- 2. 조건문
- 어떤 조건이 참일 경우에만 실행하도록 하는 것이다.
- 여기서 예약어인 if를 사용한다.
- if 조건문이 참인 경우 들여쓰기가 되어 있는 코드 부분이 실행됨
```
x = 5
if x < 10:
	print('Smaller') # Smaller가 출력됨
if x > 20:
	print('Bigger') 
	
print('Finis')       # Finis가 출력됨
```

 
- 3. 반복문
- 주어진 조건(n>0)이 참인 경우에는 들여쓰기 되어 있는 부분이 계속 실행됨
- 그렇지 않은 경우 실행을 종료하게됨
- 이 부분에서 컴퓨터는 인간보다 더 나은 수행 능력을 보임

```
n = 5
while n > 0 :  # 순차적으로 키워드인 while문에 다다르면
	print(n)   # 콜론 다음에 들여쓰기된 2줄이 하나의 반복을 만듬
	n = n - 1  # n이 0이 되면 더 이상 0보다 크지 않기 때문에 while문을 빠져나옴
print('Blastoff!') 
```