# 모두를 위한 파이썬

===========================================

## Chapter 02

### Variables, Expressions, and Statements

- 상수 (Constants) 
- 상수는 값이 변하지 않는다.

```
print(123)			 # 123 으로 출력. 123이 상수 
print(98.6)			 # 98.6 으로 출력. 98.6이 상수
print('Hello world') # Hello world로 출력. Hello world가 상수
```

- 예약어 (Reserved Words) 
- 예약어는 파이썬이 정한 의미로만 쓰이는 특별한 단어
- 예를 들어 파이썬이 if라는 예약어를 만나게 되면 조건문을 실행함
- You cannot use reserved words as variable names / identifiers


> False	 class	return	is		finally
> None	 if		for		lambda	continue
> True	 def	from	while	nonlocal
> and	 del	global	not		with
> as	 elif	try		or		yield
> assert else	import	psss
> break  except in		raise	


- 변수 (Variables) 
- 우리는 메모리에 사람이 이해할 수 있는 변수명으로 원하는 데이터를 넣을 수 있는 공간을 확보할 수 있다.
- 변수를 통해 메모리를 할당하고 이름을 지어 무언가를 그곳에 넣을 수 있다.

```
x = 12.2
print(x)  # 12.2가 출력됨
y = 14
x = 100		
print(x)  # 100이 출력됨 
```

- x, y : 메모리에 할당된 변수의 이름
- = : 할당자이며 해당 변수에 특정 값을 넣어주는 역할을 한다. (화살표와 같다)
- 12.2, 14 : 값이며 해당 변수에 사용자가 넣은 값이다.
- 변수로 선언한 뒤 해당 변수에 넣을 수 있는 값은 바꿀 수 있다.


- 변수의 이름을 정하는 규칙 (Python Variable Name Rules)

- 1. 반드시 문자 또는 underscope(_)로 시작한다. (숫자로 시작할 수 없다)
- 2. 문자와 숫자 underscope(_)를 포함할 수 있다.
- 3. 읽는 사람이 읽기 편하도록 변수명을 정하는 것이 중요

- Case1 - Worst
- 변수 이름이 길고 무작위라서 코드를 읽는 사람이 알아보기 힘듬
```
xlq3z9ocd = 35.0
xlq3z9afd = 12.50
xlq3p9afd = xlq3z9ocd * xlq3z9afd
print(xlq3p9afd)
```

- Case2 - Bad
- 위와 같은 프로그램이지만 훨씬 읽기 쉽다
```
a = 35.0
b = 12.50
c = a * b
print(c)
```

- Case3 - Good
- 의미있는 변수 이름을 지음으로써 읽는 이가 이해하기 쉽다
```
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)
```

- 파이썬은 3가지 케이스를 모두 동일하게 인지하지만 코드를 읽는 사람 입장에서는 세번째 케이스가 가장 이해하기 쉽다.


- 할당문 (Assignment Statements)
- 대입문은 오른쪽 표현의 결과를 왼쪽의 변수에 저장하는 것으로 구성되어 있다.
- 대입문은 화살표와 같은 의미이다. 오른쪽에 있는 값은 계산한 다음에 왼쪽에 있는 값을 바꾼다.

```
x = 0.6
x = 3.9 * x * (1 - x)
print(x) # 3.9 * 0.6 * (1 - 0.6)

x = 3.9 * x * (1 - x)
print(x)  # 3.9 * 0.936 * (1 - 0.936)
```
