
## 문장에 있는 단어들의 빈도 수 구하기


# split 메소드

# line = 'The general pattern to count the words'
# print(line.split())

counts = dict()
line = 'The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently.'
words = line.split()

print('Words:', words)

# 이렇게 문장을 리스트로 변환시키면 get 메소드를 활용해서 문장에 있는 단어들의 빈도 수를 구할 수 있음
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


# 딕셔너리에 루프를 적용하기
counts2 = {'chuck': 1, 'fred':42, 'jan':100}
for key in counts2:
    print(key, counts2[key])


# 딕셔너리의 키나 값을 별도로 저장하는 몇가지 방법
# 딕셔너리를 리스트로 변환하면 키로만 구성된 리스트를 얻을 수 있다

jjj = {'chunk':1, 'fred':42, 'jan':100}
print(list(jjj))

# 딕셔너리의 keys라는 메소드를 사용해도 같은 결과
print(jjj.keys())

# 딕셔너리의 값으로만 구성된 리스트를 얻으려면 values라는 메소드를 사용
print(jjj.values())

# items 메소드
print(jjj.items())

for aaa, bbb in jjj.items():
    print(aaa, bbb)