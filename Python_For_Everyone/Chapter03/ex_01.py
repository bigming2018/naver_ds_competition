# if문
# 단일 if문으로 사용하는 경우 조건문이 참인 경우에만 미리 입력해놓은 실행 코드를 실행함

# x = 5

# if x < 10:
#    print('Smaller')


# if else 문
# 첫번째 조건문의 조건이 거짓인 경우에 대해 처리하기 위해 else를 사용할 수 있음
# 즉 첫번째 if문의 조건이 거짓인 경우 else 문 이하의 실행 코드가 실행됨

#x = 11

#if x < 10:
#    print('Smaller')
#else:
#    print('Bigger')

# 다중 분기
# 하나의 조건문 블럭에 프로그래머의 필요에 의해 조건문들을 추가
# elif 라는 예약어를 사용

x = 21

if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else :
    print('Ginormous')


# try / except

astr = "123"

try:
    print("Hello")
    isInt = int(astr)
    print("World")
except:
    isInt = "Integer로 변환할 수 없습니다."

print('Done', isInt)