taxa = 1.045
investido = int(input('valor investido: '))
ano = int(input('quantidade de anos: '))
total = investido
for x in range(ano):
    total *= taxa
print('''
      ao longo de {} anos
      o investimento de {:.2f}
      rendeu {:.2f} de juros
      e o capital agora é de {:.2f}'''.format(ano,investido,total-investido,total))