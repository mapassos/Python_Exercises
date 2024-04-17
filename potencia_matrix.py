"""
Calcula a potência de uma matriz 3x3

Primeiramente é pedido ao usuário para digitar a potência, e depois cada linha da matriz.
Depois é verificado a matriz é singular ou não, ou seja, se o determinante da matriz é nulo ou não.
Note que o determinante tem que esta no intervalo (−10^-4, 10^-4) para ser considerado nulo.
Em caso positivo, a função matrix_power calcula a potência da matriz.
Por fim, a função print_matrix printa a matriz resultante na tela.

Exemplo de entrada:
3
1 2 3
4 5 4
3 2 1
"""
def main():
    A = []
    p = int(input())
    for i in range(3):
        linha = [float(x) for x in input().split()]
        A.append(linha)
    if is_singular(A):
        print_matrix(matrixPower(A, p))
        print('É singular')
    else:
        print_matrix(A)
        print('Não é singular')
    exit = input('Testar outra matriz?(y/n)')
    if exit == 'y':
        main()
    input('Aperte Enter para sair')
    return 0

def is_singular(M):
    det = 0
    matexp = [[M[i][j] if j<3 else M[i][j-3] for j in range(len(M)+2)] for i in range(len(M))]
    for i in range(3):
        detp = 1
        detm = 1
        for j in range(3):
            detp *= matexp[j][i+j]
            detm *= matexp[j][-j+2+i]
        det += (detp - detm)
    print(det)
    if det > -1e-4 and det < 1e-4:
        return True
    else:
        return False

def matrixPower(M, p):
    matprod = [[0 for j in i] for i in M]
    for i in range(2,p+1):
        matcopy = [[j for j in i] for i in matprod]
        matprod = [[0 for j in i] for i in M]
        for j in range(len(M)):
            for k in range(len(M[j])):
                for l in range(len(M)):
                    if i == 2:
                        matprod[j][k] += (M[j][l] * M[l][k])
                    else:
                        matprod[j][k] += (M[j][l] * matcopy[l][k])
    return matprod

def print_matrix(M):
    for linha in M:
        print(f'{linha[0]:.2f} {linha[1]:.2f} {linha[2]:.2f}')

if __name__ == '__main__':
    main()