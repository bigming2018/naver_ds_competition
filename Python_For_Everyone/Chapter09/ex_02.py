# get 메소드

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# counts.get(name,0) : counts 딕셔너리에 name이라는 키가 존재할 경우 name 에 대한 값을 불러오고
# 그렇지 않을 경우 counts 딕셔너리에 name 이라는 키에 0이라는 데이터를 추가

