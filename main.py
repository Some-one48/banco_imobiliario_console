import csv
from random import randint # pip install
import os 
import time
from colorama import init, Fore, Back, Style # pip install

players = []
sit = [
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
    [0,0,0,0,0,'none'],
]

def dado():
    dado = randint(1,6)
    return dado

def header():
    print('----------------------------------')
    print('\tBANCO IMOBILIÁRIO')
    print('----------------------------------')

def newPlayer(p:list):
    for i in range(len(p)):
        player = {
            'ordem': len(players)+1,
            'casa_atual': 0,
            'nome': p[len(players)],
            'saldo': 805,
            'propriedades_position': []
        }
        players.append(player)

def vezDe(qtd:int, ordem:int):
    if ordem == 1:
        return 2
    else:
        return 1

def acoes(dado:int, o:int):
    p = players[o-1]
    saldo = p['saldo']

    p['casa_atual'] += dado
    casa = p['casa_atual']

    with open('terrenos.csv', 'r') as file:
        reader = list(csv.reader)
        parou = reader[casa]

        print(parou[1])
        print(f'Preço: {parou[2]}')

    print(f'\nSaldo Atual: {saldo}')
    print('O que deseja fazer?\n')
    print('1. Comprar a propriedade')
    print('2. Ver suas propriedades')
    print('3. Continuar / Pular')
    a = int(input('\nDigite sua operação: '))

    if a not in [1,2,3]:
        print('\n')
        print(Back.RED + 'ERRO:' + Back.RESET + Fore.RED +'Digite uma operação válida' + Fore.RESET)
        acoes(dado, o)
    else:
        print('All right :D')

if __name__ == '__main__':
    finish = False

    # INICIO
    print('----------------------------------------------')
    print('\tBEM-VINDO AO BANCO IMOBILIÁRIO')
    print('----------------------------------------------')

    qtd_j = int(input('Digite a quantidade de jogadores: '))

    jogadores = []
    for i in range(qtd_j):
        temp = input(f'Digite o nome do jogador {i+1}: ')
        jogadores.append(temp)
    
    print('\n--------------------------------')
    print('\tORDEM DE JOGADA:')
    print('--------------------------------')
    for i in range(len(jogadores)):
        print(f'{i+1}. {jogadores[i]}')
        newPlayer(jogadores)

    time.sleep(2)
    os.system("cls")

    while(finish == False):
        header()
        ordem = 0
        ordem = vezDe(2, ordem)
        print('Vez de', end=' ')
        print(Back.WHITE + Fore.BLACK + f'{jogadores[ordem-1]}' + Back.RESET + Style.NORMAL + Fore.RESET)
        
        dd = dado()
        print(f'Dado: {dd}')

        acoes(dd, 1)