# 루프의 활용
# 1. 루프를 사용하여 개수 세기
# 리스트에 몇 개의 원소가 있는지를 알고자할 때 루프를 사용할 수 있음

zork = 0
print('Before', zork)

numbers = [9,41,12,3,74,15]  # numbers라는 int를 원소로 가지는 list를 선언

for thing in numbers:
    zork = zork + 1
    print(zork, thing)
print('After', zork)