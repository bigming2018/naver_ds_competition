abc = 'With three words'
stuff = abc.split()
print(stuff)


# 구분자
words2 = 'first;second;third'
stuff2 = words2.split()
print(stuff2)

stuff3 = words2.split(';')
print(stuff3)


# 이메일 주소 추출하기
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

words = line.split()

print(words)
print(words[1])

email = words[1]
address = email.split('@')
print(address)
print(address[1])


test = ['Hello', 'World']
test.append(['Connect', 'Foundation', 'Education'])
print(len(test))


# 딕셔너리
purse = dict()
purse['money'] = 12     # 'money'라는 키에 12라는 값 연결
purse['candy'] = 3      # 'candy'라는 키에 3이라는 값 연결
purse['tissues'] = 75   # 'tissues'라는 키에 75라는 값 연결

print(purse)  # 입력한 순서대로 나오지만 항상 입력한 순서대로 출력되는 것은 아님

print(purse['candy'])  # candy 라는 키에 저장도니 값에 접근하려면 대괄호 안에 키를 넣어서 접근할 수 있음

purse['candy'] = purse['candy'] + 2   # 접근한 내용을 업데이트
print(purse)