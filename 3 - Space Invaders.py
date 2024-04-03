import math

def intersecta(x, y, vx, vy, cx, cy, r):
    # PARÂMETROS: 1) a posição (x,y) e a direção (vx,vy) do raio laser disparado,
    #             2) o centro (cx,cy) e o raio r de um círculo.
    # RETORNO: True caso o raio laser intersecte o círculo ou
    #          False caso contrário.
    if r < 0:
        return False
    if vx != 0 and vy != 0:
        ang = vy / vx
        A = - ang
        B = 1
        C = - y + ang * x
    elif vx == 0 and vy == 0:
        return False
    elif vy != 0:
        A = 1
        B = 0
        C = -x
    else:
        A = 0
        B = 1
        C = -y
    dx = x - cx
    dy = y - cy
    d = math.sqrt(dx ** 2 + dy ** 2)
    if d <= r:
        return True
    inv = 1 / (A ** 2 + B ** 2)
    cond = abs(A * cx + B * cy + C) * math.sqrt(inv)
    if cond > r + 0.0001:
        return False
    else:
        con = (A * cx + B * cy + C)
        delta = math.sqrt(r ** 2 * (A ** 2 + B ** 2) - con ** 2)
        xnew1 = inv * (A * con + B * delta) + cx
        ynew1 = inv * (-A * delta + B * con) + cy
        if xnew1 < x and vx >= 0 or xnew1 > x and vx <= 0:
            return False
        if ynew1 < y and vy >= 0 or ynew1 > y and vy <= 0:
            return False
        return True


def explode(cx, cy, r):
    # PARÂMETROS: o centro (cx,cy) e o raio r de um círculo que será explodido.
    # RETORNO:  uma lista de 4 novos cículos com as seguintes propriedades
    #           1º círculo -> centro (cx + r, cy) e raio r/2
    #           2º círculo -> centro (cx - r, cy) e raio r/2
    #           3º círculo -> centro (cx, cy - r) e raio r/2
    #           4º círculo -> centro (cx, cy + r) e raio r/2
    c1x, c1y, c1r = cx + r, cy, r / 2
    c2x, c2y, c2r = cx - r, cy, r / 2
    c3x, c3y, c3r = cx, cy - r, r / 2
    c4x, c4y, c4r = cx, cy + r, r / 2
    return [c1x, c1y, c1r, c2x, c2y, c2r, c3x, c3y, c3r, c4x, c4y, c4r]

# Quantidade de círculos iniciais
M = int(input())

# Status dos círculos:
# 2 -> círculo original,
# 1 -> círculo filho,
# 0 -> círculo inexistente

# Inicializa status
life = M * [2]

# Listas auxiliares
CX = []  # posição x dos centros dos círculos
CY = []  # posição y dos centros dos círculos
R = []  # raio dos círculos

# Carrega as informações dos círculos iniciais
for i in range(M):
    cx, cy, r = [float(x) for x in input().split()]
    CX.append(cx)
    CY.append(cy)
    R.append(r)

# Inicializa os disparos de raios
N = int(input())
for i in range(N):
    # Carrega informações de um raio
    x, y, vx, vy = [float(k) for k in input().split()]

    # Itera sobre os círculos
    L = len(CX)
    for j in range(L):
        # se o circulo esta vivo
        if life[j] > 0:
            # se o raio intersecta o círculo
            if intersecta(x, y, vx, vy, CX[j], CY[j], R[j]):
                # se o círculo é original ele explode
                if life[j] > 1:
                    # cria novos círculos
                    children = explode(CX[j], CY[j], R[j])
                    # insere as informações dos novos círculos nas listas CX, CY e R
                    for k in range(4):
                        CX.append(children[k * 3 + 0])
                        CY.append(children[k * 3 + 1])
                        R.append(children[k * 3 + 2])
                        # os novos circulos sao marcados como filhos
                        life.append(1)
                # circulo j morre
                life[j] = 0

# Conta quantos círculos sobreviveram
count = 0
for i in life:
    if i > 0:
        count += 1

# Imprime a quantidade de círculos sobreviventes
print(count)
