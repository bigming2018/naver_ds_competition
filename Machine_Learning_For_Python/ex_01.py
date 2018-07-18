
# 일반 코드

colors = ["red", "blue", "green", "yellow"]
result = ""

for s in colors:
    result += s

print(result)

# pythonic code

colors = ["red", "blue", "green", "yellow"]
result = "".join(colors)

print(result)