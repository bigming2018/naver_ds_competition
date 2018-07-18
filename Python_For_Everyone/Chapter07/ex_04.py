# 파일 내용 검색하기
fhand = open('C:\\Users\\Administrator\\Desktop\\hello.txt')
for line in fhand:
    if line.startswith('텍스트'):
        print(line)


fhand2 = open('C:\\Users\\Administrator\\Desktop\\hello.txt')
for line2 in fhand2:
    line2 = line2.rstrip() # 오른쪽 공백 제거
    if line2.startswith('텍스트'):
        print(line2)


# 파일 이름 입력받기
# 사용자가 파일의 이름을 직접 입력하는 경우
fname = input('Enter the file name: ')
try:
    fhand3 = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('텍스트'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
