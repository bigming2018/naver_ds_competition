# 머신러닝을 위한 Pyyhon

===========================================

### Pythonic Code - Split & Join
- Split & Join 을 사용하여 String Type 의 값을 List 형태로 변환하고
- List Type 의 값을 String Type의 값으로 변환


### 빈칸을 기준으로 문자열 나누기

```
items = 'zero one two three'.split()
print(items)
```

### ","을 기준으로 문자열 나누기

```
example = 'python,jquery,javascrpt'

print(example.split(","))
```


### 리스트의 각 값을 a, b, c 변수로 unpacking

```
example = 'python,jquery,javascript'

a, b, c = example.split(",")
```

### "."을 기준으로 문자열 나누고 unpacking

```
example = 'cs50.gachon.edu'

subdomain, domain, tld = example.split(".")
```