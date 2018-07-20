# split

# 빈칸 기준
items = 'zero one two three'.split()
print(items)

# 콤마 기준
example = '스타크래프트,디아블로,오버워치'
print(example.split(","))


# unpacking
example = '수지,박보영,아이유'

a, b, c = example.split(",")

print(a,b,c)

# unpacking
example2 = 'codud2003.naver.com'

subdomain, domain, tld = example2.split(".")

print(subdomain, domain, tld)


# list Comprehension

# for loop + append
result = []

for i in range(10):
    result.append(i)

print(result)


# list Comprehension
result2 = [i for i in range(10)]
print(result2)

result3 = [i for i in range(10) if i % 2 == 0]
print(result3)


# Nested For loop
word_1 = "Hello"
word_2 = "World"
results = [i+j for i in word_1 for j in word_2]

print(results)


# Nested For loop + if 문
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]

results2 = [i+j for i in case_1 for j in case_2]
print(results2)


# if 문 추가
results3 = [i+j for i in case_1 for j in case_2 if not(i==j)]
results3.sort()

print(results3)


# split + list Comprehension

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
    print(i)