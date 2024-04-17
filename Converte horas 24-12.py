'''
Implementação de um função que converte um horario da notação de 24 horas para a notação de 12 horas (AM/PM).

Exemplo de entrada:
17:35
13:30
09:40
06:00
-1
'''

def main():
    while True:
        horario = input()
        if horario=='-1':
            break
        else:
            print(converte(horario))
    input('Pressione Enter para sair')


def converte(horario):
    if int(horario[:2]) < 12:
        if int(horario[:2]) == 0:
            con = str(abs(int(horario[:2]) - 12))
            return con + horario[2:] + ' A.M'
        else:
            return horario + ' A.M'
    else:
        if int(horario[:2]) == 12:
            return horario + ' P.M'
        else:
            con = str(int(horario[:2]) - 12)
            if len(con) == 1:
                con = '0' + con
            return con + horario[2:] + ' P.M'

if __name__ == '__main__':
    main()