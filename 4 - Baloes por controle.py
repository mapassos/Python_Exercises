import math


def dist(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def limite(x, y, dir, sinal):
    if dir == 'S':
        if math.sqrt(x ** 2 + (y + 10) ** 2) > 2001:
            return True
    elif dir == 'F' or dir == 'V':
        if x <= 0 and sinal == '-':
            if math.sqrt((x - 10) ** 2 + y ** 2) > 2001:
                return True
        elif x >= 0 and sinal == '+':
            if math.sqrt((x + 10) ** 2 + y ** 2) > 2001:
                return True
    return False


def movimento(x, y, dir, sinal):
    if limite(x, y, dir, sinal):
        return x, y, sinal
    if dir == 'S' and y < 200:
        y += 10
    elif dir == 'D' and y != 0:
        y -= 10
    elif dir == 'F' and y != 0:
        if sinal == '+':
            x += 10
        else:
            x -= 10
    elif dir == 'V' and y != 0:
        if sinal == '+':
            x += 10
            sinal = '-'
        else:
            x -= 10
            sinal = '+'
    return x, y, sinal


x, y = 0, 0
sinal = '+'
num = int(input())
for i in range(num):
    comando = input()
    x, y, sinal = movimento(x, y, comando, sinal)
print(abs(y), abs(x))
