print('Привет! Это игра Жизнь.')
print('Правила игры:')
print('На прямой расположены живые клетки, у каждой клетки два соседа.')
print('У первой клетки соседом слева является крайняя правая клетка и наоборот.')
print('Существуют правила зарождения и гибели клеток:')
print('Живая клетка с двумя соседями - умирает')
print('Нет соседей - умирает')
print('Один сосед - продолжает жить')
print('В пустой клетке, если есть один сосед, то зарождается жизнь')
print('Если есть два соседа - не рождается')
print('Если нет соседей - не рождается')
print('Пробел - нет жизни, "*" - есть жизнь.')

print('Выберите: вы вводите мир(1) или мир генерируется сам(2)')
abc = input()
if abc == '1':
    print('Введите длину мира.')
    a = int(input()) # длина мира
    print('ведите мир.')
    print('Пробел - нет жизни, "*" - есть жизнь.')
    print('Пример ввода: "*  * "')
    d = input() # мир
    while len(d) != a:
        print('Длина введённого мира не соответствует изначально вводимой длине.')
        print('Изначальная длина:', str(a) + '.')
        d = input()
    print('Введите количество поколений.')
    c = int(input()) # количество поколений
else:
    a = 5
    d '* *  '
    c = 5
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
