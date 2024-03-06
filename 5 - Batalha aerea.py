def jogada(jog, pos):
    jog[linhas[pos[0]]][int(pos[1]) - 1] = 0
    return jog


def jogo(jog1, jog2, num_jog):
    for i in range(1, num_jog + 1):
        pos = input()
        if i % 2:
            jog2 = jogada(jog2, pos)
        else:
            jog1 = jogada(jog1, pos)
    j1 = sum(j for i in jog1 for j in i)
    j2 = sum(j for i in jog2 for j in i)
    return (j1, j2)


num_jog = int(input())
linhas = {chr(i): (i - ord('A')) for i in range(ord('A'), ord('A') + 9)}
jogA = [[int(j) for j in input().split()] for i in range(9)]
input()
jogB = [[int(j) for j in input().split()] for i in range(9)]
input()

res = jogo(jogA, jogB, num_jog)

if res[0] > res[1]:
    print('O jogador A venceu')
elif res[0] < res[1]:
    print('O jogador B venceu')
else:
    print('Empate')