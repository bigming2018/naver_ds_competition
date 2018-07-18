# 사람의 방식으로 빈도 수 세기

# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)

# ccc['cwen'] = ccc['cwen'] + 1
# print(ccc)

# ccc = dict()
# 'csev' in ccc  # ccc라는 딕셔너리 안에 'csev' 라는 값이 있는지 확인하기 위해 in 연산자를 사용하면 참(True) 또는 거짓(False)라고 알려줌

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name in counts:
        counts[name] = counts[name] + 1
    else:
        counts[name] = 1
print(counts)


# not 연산자를 사용해서 동일하게 해결할 수도 있음

counts2 = dict()
names2 = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts2:
        counts2[name] = 1
    else:
        counts2[name] = counts[name] + 1
print(counts2)