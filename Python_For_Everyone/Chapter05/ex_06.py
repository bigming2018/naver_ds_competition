# 반복문 응용
# 2. 루프를 사용하여 합계 구하기
# 각 원소를 누적해서 더해 총합을 알아낼 수 있다.

zork = 0
print('Before', zork)

numbers = [9,41,12,3,74,15]

for thing in numbers:
    zork = zork + thing
    print(zork, thing)
print('After', zork)