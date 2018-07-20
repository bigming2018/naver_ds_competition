# 머신러닝을 위한 Pyyhon

===========================================

### Pythonic Code - List Comprehension
- List Comprehension 은 파이썬에서 가장 많이 사용되는 기법 중에 하나


### for loop _ append 사용하기

```
result = []

for i in range(10):
    result.append(i)

print(result)
```


### list Comprehension 사용하기

```
result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)
```


### split + list Comprehension

```
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
    print(i)
```