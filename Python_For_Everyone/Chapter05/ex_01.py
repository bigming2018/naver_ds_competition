# while 루프

n = 5

while n > 0:
    print(n)
    n = n - 1

print("Bang!")
print(n)


# break문
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')