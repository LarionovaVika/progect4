a = int(input()) # длина мира
d = input() # мир
c = int(input()) # количество поколений
b = []
for i in d.split('1'):
    b.append([i])
for u in range(c):
    for y in range(a - 1):
        if y == 0:
            if b[y] == '*':
                if b[y + 1] == '*' and b[a - 1] == '*':
