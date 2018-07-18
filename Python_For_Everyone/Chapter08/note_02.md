# 모두를 위한 파이썬

===========================================

## Chapter 08


### 리스트를 활용해 원하는 값 추출하기

### 문자열과 리스트
- 문자열과 리스트는 잘 어울려 사용됨


### 구분자
- 명시적으로 구분자를 넣어주지 않으면 빈칸을 구분자로 인지하고 나누게 됨


### 이메일 주소 추출하기
```
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# line에 uct.ac.za만 추출하기

words = line.split()
# words는 해당 라인을 빈칸을 구분자로 하여 리스트로 저장

print(words[1])
# stephen.marquard@uct.ac.za 가 출력

email = words[1]
address = email.split('@')
print(address)
# ['stephen.marquard', 'utc.ac.za'] 가 출력됨

print(address[1])
# uct.ac.za 가 출력
```