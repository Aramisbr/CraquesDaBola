print (f'{'===  CRAQUES DA BOLA ===':^30}')

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ').capitalize()
    part = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for p in range(1, part+1):
            partidas.append(int(input(f'      Gols na partida {p}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? S/N ').upper().strip()[0]
        if resp in 'SN':
            break
        print ('ERRO! Tente novamente.')
    if resp == 'N':
        break
print ('=-' * 30)

time = sorted(time, key=lambda x: x['Total'], reverse=True)

print ('Cod. ', end='')
for k in jogador.keys():
    print (f'{k:<15}', end='')
print()
print ('-' * 40)
for k, v in enumerate (time):
    print (f'{k+1:>3}  ', end= '')
    for d in v.values():
        print (f'{str(d):<15} ', end='')
    print()
print ('-' * 40)

while True:
    busca = int(input('Digite o código do jogador para consultar (999 para sair): '))
    if busca == 999:
        break
    if busca <1 or busca > len(time):
        print (f'ERRO: Jogador não encontrado, tente digitar entre 1 e {len(time)}.')
    else:
        print (f' ----DADOS DO JOGADOR {time[busca-1]["Nome"]} ----')
        for i, g in enumerate (time[busca-1]['Gols']):
            print (f'Na partida {i+1} o jogador {time[busca-1]["Nome"]} fez {g} gols.')
    print ('-' * 40)
print ('<<<<< VOLTE SEMPRE >>>>>')
