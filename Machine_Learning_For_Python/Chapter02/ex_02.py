# Enumerate
# List의 element를 추출할 때 번호를 붙여서 추출
for i, v in enumerate(['tic', 'tac', 'toe']): # i에는 인덱스번호, v는 value 값
        print(i, v)


mylist = ["a", "b", "c", "d"]
list(enumerate(mylist))  # list의 있는 index와 값을 unpacking 하여 list로 저장

print(list(enumerate(mylist)))


print({i:j for i,j in enumerate('Gachon University is an academic institute located in South Korea.'.split())})
# 문장을 list 로 만들고 list의 index와 값을 unpacking하여 dict로 저장

# zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):  # 병렬적으로 값을 추출
    print(a,b)


# 각 tuple의 같은 index끼리 묶음
a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)

# 각 Tuple 같은 index를 묶어 합을 list로 변환
print([sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))])