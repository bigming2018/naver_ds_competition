# 루프의 응용
# for 루프를 이용해 가장 큰 수를 찾아내기

largest_so_far = -1
print('Before', largest_so_far)

numbers = [9, 41, 12, 3, 74, 15]

for the_num in numbers:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print('largest_so_far:', largest_so_far, 'current number: ', the_num)


print('After', largest_so_far)