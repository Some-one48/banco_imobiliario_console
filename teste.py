import csv
from random import randint # pip install
import os 
import time
from colorama import init, Fore, Back, Style # pip install

players = []

p = ['Fulano', 'Sicrano']
for i in range(len(p)):
    player = {
        'ordem': len(players)+1,
        'casa_atual': 0,
        'nome': p[len(players)],
        'saldo': 805,
        'propriedades_position': []
    }
    players.append(player)

def acoes(dado:int, o:int):
    p = players[o-1]

    p['casa_atual'] += dado

    with open('terrenos.csv', 'r') as file:
        reader = list(csv.reader(file))
        parou = reader[p['casa_atual']]

        print(parou[1])
        print(f'Preço: {parou[2]}')
    
    with open('sit.csv', 'r') as file2:
        reader2 = list(csv.reader(file2))
        parou2 = reader2[p['casa_atual']]


    if parou[0] not in ['3','17','25'] and parou2[6] in ['none', 'banco']:
        print(f'\nSaldo Atual: R${p['saldo']}')
        print('O que deseja fazer?\n')
        print('1. Comprar a propriedade')
        print('2. Ver suas propriedades')
        print('3. Continuar / Pular')
        a = int(input('\nDigite sua operação: '))

        if a == 1:
            custo = int(parou[2])
            p['saldo'] -= custo
            p['propriedades_position'].append(parou[0])
            with open('sit.csv', 'r') as f:
                rid = list(csv.reader(f))
                pr = rid[p['casa_atual']]

                for i in range(1,6):
                    if pr[i] == '0':
                        pr[i] = '1'
                        pr[6] = p['nome']
                        break
                    else:
                        continue
            
        elif a == 2:
            for prop in p['propriedades_position']:
                with open('terrenos.csv', 'r'):
                    ...

        elif a == 3:
            ...
        else:
            print('\n')
            print(Back.RED + 'ERRO:' + Back.RESET + Fore.RED +'Digite uma operação válida' + Fore.RESET)
            acoes(0, o)
    else:
        p['saldo'] -= 30
        print('\nDívida paga ao Banco')
        print(f'Saldo Atual: R${p['saldo']}')

acoes(3,2)