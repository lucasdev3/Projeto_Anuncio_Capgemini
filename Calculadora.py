import os
while True:
    try:
        investimento_dia = int(input("Valor a ser investido: R$"))
        break
    except ValueError:
        print('Digite somente valores inteiros...')
views_init = 30 * investimento_dia
cliques = 0.12 * views_init
compartilhamentos_max = (cliques * 0.15) * 4
new_views = int(compartilhamentos_max * 40)
total_views = new_views + views_init

print("Valor Investido: R${:.2f} | Projeção de Alcance: {} visualizacoes".format(investimento_dia, total_views))
print(cliques)