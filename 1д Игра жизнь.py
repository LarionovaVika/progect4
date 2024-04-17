a = int(input()) # длина мира
d = input() # мир
while len(d) != a:
    print('Длина введённого мира не соответствует изначально вводимой длине.')
    print('Изначальная длина:', str(a) + '.')
    d = input()
c = int(input()) # количество поколений
b = [] # мир для изменений
e = [] # получившийся мир
f = 0 # счётчик для определения осталась жизнь или нет
for i in d:
    b.append([i])
    e.append([i])
print(e)
for u in range(c):
    for q in e:
        if q[0] == '*':
            f = 1
    if f == 0:
        break
    for y in range(a):
        if y == 0:
            if b[y][0] == '*':
                if b[y + 1][0] == '*' and b[a - 1][0] == '*':
                    e[y][0] = ' '
                elif b[y + 1][0] == ' ' and b[a - 1][0] == ' ':
                    e[y][0] = ' '
            else:
                if b[y + 1][0] == '*' and b[a - 1][0] == ' ':
                    e[y][0] = '*'
                elif b[y + 1][0] == ' ' and b[a - 1][0] == '*':
                    e[y][0] = '*'
        elif y == a - 1:
            if b[y][0] == '*':
                if b[y - 1][0] == '*' and b[0][0] == '*':
                    e[y][0] = ' '
                elif b[y - 1][0] == ' ' and b[0][0] == ' ':
                    e[y][0] = ' '
            else:
                if b[y - 1][0] == '*' and b[0][0] == ' ':
                    e[y][0] = '*'
                elif b[y - 1][0] == ' ' and b[0][0] == '*':
                    e[y][0] = '*'
        else:
            if b[y][0] == '*':
                if b[y - 1][0] == '*' and b[y + 1][0] == '*':
                    e[y][0] = ' '
                elif b[y - 1][0] == ' ' and b[y + 1][0] == ' ':
                    e[y][0] = ' '
            else:
                if b[y - 1][0] == '*' and b[y + 1][0] == ' ':
                    e[y][0] = '*'
                elif b[y - 1][0] == ' ' and b[y + 1][0] == '*':
                    e[y][0] = '*'
    b = []
    f = 0
    for t in e:
        for r in t:
            b.append([r])
    print(e)

    print(e)
