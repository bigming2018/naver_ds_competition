# continue

while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# continue 는 loop의 시작점으로 다시 돌아가서 loop를 실행함
# break는 loop 끝나는 점 바로 다음에 오는 코드를 실행