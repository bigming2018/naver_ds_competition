# 파일 읽기
# 텍스트 파일을 읽어온 후 내장 함수를 활용해 특정 문자열의 개수를 알아낼 수 있음

# 파일 핸들
# 파일 핸들(File Handle)은 순서가 있고 연속적으로 구성된 텍스트 파일을 한줄한줄 읽어나가게 됨

# fhand = open('C:\\Users\\Administrator\\Desktop\\hello.txt')

# for line in fhand:
#    print(line)


# 파일의 라인 수 세기
fhand = open('C:\\Users\\Administrator\\Desktop\\hello.txt')
count = 0

for line in fhand:
    count = count + 1
print('Line Count:', count)



# 파일 전체 읽기
# 전체 텍스트 파일을 단일한 하나의 문장으로 읽기
fhand2 = open('C:\\Users\\Administrator\\Desktop\\hello.txt')
inp = fhand2.read()
print(len(inp))
print(inp[:20])