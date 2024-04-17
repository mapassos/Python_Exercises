'''
Implementação de função que avalia qual estação uma data digitada inserida pelo usuário pertence
Um exemplo do formato de entrada pode ser visto abaixo.

Exemplo de entrada:
23 de setembro
21/06
21 de março
-1
'''

def main():
    while True:
        data = input()
        if data == '-1':
            break
        else:
            print(estacao_do_ano(data))


def estacao_do_ano(data):
    mes = {
        'janeiro': '01',
        'fevereiro': '02', 
        'março': '03', 
        'abril': '04', 
        'maio': '05', 
        'junho': '06', 
        'julho': '07', 
        'agosto': '08', 
        'setembro': '09', 
        'outubro': '10', 
        'novembro': '11', 
        'dezembro': '12'
        }
    data = data.split()
    r = ''
    if len(data)>1:
        if len(data[0]) == 1:
            r = '0'
        r = r + data[0] + '/' + mes[data[2]]
    else:
        r = data[0]
    if int(r[-2:]) < 3 or int(r[:2]) <= 20 and int(r[-2:]) == 3:
        return 'Verão'
    elif int(r[-2:]) < 6 or int(r[:2]) <= 20 and int(r[-2:]) == 6:
        return 'Outono'
    elif int(r[-2:]) < 9 or int(r[:2]) <= 20 and int(r[-2:]) == 9:
        return 'Inverno'
    elif int(r[-2:]) < 12 or int(r[:2]) <= 20 and int(r[-2:]) == 12:
        return 'Primavera'
    else:
        return 'Verão'


if __name__ == '__main__':
    main()
