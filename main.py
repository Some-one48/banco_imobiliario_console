import csv
from random import randint
import os 
import time
from colorama import init, Fore, Back, Style

def dado():
    dado = randint(1,6)
    return dado

def header():
    print('----------------------------------------------')
    print('\tBEM-VINDO AO BANCO IMOBILIÁRIO')
    print('----------------------------------------------')

def newPlayer(players:list):
    wPlay = []
    for i in range(len(players)):
        player = {
            'ordem': i+1,
            'nome': players[i],
            'saldo': 805,
            'propriedades_id': []
        }
        wPlay.append(player)

    with open('players.csv', 'w') as file:
        dados = csv.DictWriter(file, fieldnames=['ordem', 'nome', 'saldo', 'propriedades_id'], lineterminator='\n')
        dados.writeheader()

        for p in wPlay:
            dados.writerow(p)
    
def vezDe(players:list):
    atual = 1
    passado = 0
    if len(players) == 2:
        if passado == 1:
            passado = 1
            return players[0]
        else:
            return

if __name__ == '__main__':
    finish = False
    # INICIO
    header()

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

    #
    header()
    #while(finish == False):
    print('Vez de', end=' ')
    print(Back.WHITE + Style.BRIGHT + f'{jogadores[0]}' + Back.RESET + Style.NORMAL)
    
    dd = dado()
    print(f'Dado: {dd}')