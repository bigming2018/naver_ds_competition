# 리스트 병합

a = [1,2,3]
b = [4,5,6]
c = a + b

print(c)

t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])


# dir() 메소드
x = list()
print(dir(x))


# 리스트 만들기
# 빈 리스트 만들기 - 항목 추가하기 - 항목 정렬하기 - in 을 활용해 'Glenn' 이 친구 목록에 있는지 확인
friends = list()
friends.append('Joseph')
friends.append('Glenn')
friends.append('Sally')

print(friends)

friends.sort()
print(friends)

print('Glenn' in friends)