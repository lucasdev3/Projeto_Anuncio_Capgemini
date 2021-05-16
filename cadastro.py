from datetime import datetime
from calculaDatas import getDifference
from time import sleep
import os
from openpyxl import *


id = 1
l = 2
cont = 0
banco = {}
bancoFiltroDataMaior = {}
bancoFiltroDataMenor = {}
bancoFiltroCliente = {}

# ---------------- INICIANDO A TABELA EM EXCEL -----------------
wb = load_workbook(filename='banco_de_dados.xlsx')
sh = wb.worksheets[0]
# ------------------------------CADASTRO------------------------

while True:
    try:
        qnt = int(input('Quantos anuncios gostaria de cadastrar? '))
        print('\n')
        break
    except ValueError as e:
        print('Digite apenas numeros inteiros...', e)

while cont < qnt:
    gradeGeral = []
    gradeCadastro = []
    gradeRelatorio = []
    gradeFiltroDataMaior = []
    gradeFiltroDataMenor = []
    gradeCadastroMaiorSete = []
    gradeRelatorioMaiorSete = []
    gradeCadastroMenorSete = []
    gradeRelatorioMenorSete = []

    anuncio = input('Nome do anuncio: ').title().strip()
    sh[f'C{l}'] = anuncio
    gradeCadastro.append(anuncio)
    cliente = input('Nome do cliente: ').title().strip()
    sh[f'B{l}'] = cliente
    gradeCadastro.append(cliente)
    dataInicio = input('Data de inicio Exemplo [ 20-05-2000 ]: ').strip()
    sh[f'D{l}'] = dataInicio
    gradeCadastro.append(dataInicio)
    dataTermino = input('Data de término Exemplo [ 20-05-2000 ]: ').strip()
    sh[f'E{l}'] = dataTermino
    gradeCadastro.append(dataTermino)
    while True:
        try:
            investimentoDia = int(input('Investimento diário: R$ '))
            sh[f'F{l}'] = investimentoDia
            gradeCadastro.append(investimentoDia)
            break
        except ValueError as e:
            print('Digite somente numeros inteiros...', e)
    # ------------------------ CRIAÇÃO DA GRADE DE RELATORIO -----------------
    # ----------------------------CALCULO DE RELATORIO -----------------------

    a1 = int(dataInicio[6:12])
    m1 = int(dataInicio[3:5])
    d1 = int(dataInicio[0:2])

    a2 = int(dataTermino[6:12])
    m2 = int(dataTermino[3:5])
    d2 = int(dataTermino[0:2])

    inicio = datetime(a1, m1, d1)  # yr, mo, day, hr, min, sec
    fim = datetime(a2, m2, d2)

    viewsInit = 30 * investimentoDia
    cliques = viewsInit * 0.12
    sh[f'I{l}'] = cliques
    compartilhamentos = (0.15 * cliques) * 4
    sh[f'J{l}'] = compartilhamentos
    newViews = int(compartilhamentos * 40)
    totalViews = int(viewsInit + newViews)
    sh[f'H{l}'] = totalViews
    investimentoTotal = investimentoDia * (getDifference(inicio, fim, 'days'))
    sh[f'G{l}'] = investimentoTotal
    gradeRelatorio.append(investimentoTotal)
    gradeRelatorio.append(totalViews)
    gradeRelatorio.append(cliques)
    gradeRelatorio.append(compartilhamentos)

    gradeRelatorioMenorSete = gradeRelatorio
    gradeCadastroMenorSete = gradeCadastro
    gradeRelatorioMaiorSete = gradeRelatorio
    gradeCadastroMaiorSete = gradeCadastro

    # ----------------------FILTRAR POR DATA COLOCANDO AS INFORMAÇÕES EM LISTAS DIFERENTES --------------------

    # ANUNCIOS COM MAIS DE 7 DIAS
    if getDifference(inicio, fim, 'days') > 7:
        gradeFiltroDataMaior.append(gradeCadastroMaiorSete)
        gradeFiltroDataMaior.append(gradeRelatorioMaiorSete)
    # ANUNCIOS COM MENOS DE 7 DIAS
    else:
        gradeFiltroDataMenor.append(gradeCadastroMenorSete)
        gradeFiltroDataMenor.append(gradeRelatorioMaiorSete)
    bancoFiltroDataMaior[id] = gradeFiltroDataMaior
    bancoFiltroDataMenor[id] = gradeFiltroDataMenor
    # RETIRANDO CHAVES COM LISTAS VAZIAS
    while bancoFiltroDataMenor[id] == []:
        bancoFiltroDataMenor.pop(id)
        break
    while bancoFiltroDataMaior[id] == []:
        bancoFiltroDataMaior.pop(id)
        break

    # ----------------- CADASTROS E RELATORIOS GERAIS ----------------------------------

    gradeGeral.append(gradeCadastro)
    gradeGeral.append(gradeRelatorio)

    banco[id] = gradeGeral

    # ------------------------ FILTRO DE CLIENTES ---------------------------

    bancoFiltroCliente[cliente] = gradeGeral

    # -------------------------------------------------------------------------

    id += 1
    cont += 1
    l += 1
    print('\n')
# ------------------------IMPRESSÃO DE DADOS NA TELA PARA O USUÁRIO MOSTRANDO OS ANUNCIOS E SEUS RELATORIOS----------

titulo2 = 'GERANDO RELATORIO'
print('-' * len(titulo2))
print(titulo2)
print('-' * len(titulo2))
sleep(4)
# ----------------------------- RELATORIO GERAL ------------------------------------
for i, j in banco.items():
    cadastro = banco[i][0]
    relatorio = banco[i][1]
    print('\n')
    print(
        'ID Anuncio: {} | Cliente: {} | Anuncio: {} | Data de Inicio: {} | Data de Termino: {} | Investimento Inicial: R${:.2f}'.format(
            i, cadastro[1], cadastro[0], cadastro[2], cadastro[3], float(cadastro[4])))
    print('\n')
    print(
        'Investimento Total: R${:.2f} | Vizualizacoes Max.: {} | Cliques Max.: {} | Compartilhamentos Max.: {}'.format(
            float(relatorio[0]), relatorio[1], relatorio[2], int(relatorio[3])))
    print('\n')

print('\n')
# ------------------ RELATORIO  POR TEMPO --------------------------------
filtroData = input('Gostaria de filtrar os anuncios por data?[S / N]: ').strip().lower()
# --------------------MAIS DE 7 DIAS ---------------------
if filtroData == 's':
    titulo3 = 'FILTRANDO ANUNCIOS COM MAIS DE 7 DIAS '
    print('-' * len(titulo3))
    print(titulo3)
    print('-' * len(titulo3))
    sleep(4)
    for i, j in bancoFiltroDataMaior.items():
        cadastro = bancoFiltroDataMaior[i][0]
        relatorio = bancoFiltroDataMaior[i][1]
        print('\n')
        print(
            'ID Anuncio: {} | Cliente: {} | Anuncio: {} | Data de Inicio: {} | Data de Termino: {} | Investimento Inicial: R${:.2f}'.format(
                i, cadastro[1], cadastro[0], cadastro[2], cadastro[3], float(cadastro[4])))
        print('\n')
        print(
            'Investimento Total: R${:.2f} | Vizualizacoes Max.: {} | Cliques Max.: {} | Compartilhamentos Max.: {}'.format(
                float(relatorio[0]), relatorio[1], int(relatorio[2]), int(relatorio[3])))
        print('\n')

    print('\n')

    titulo4 = 'FILTRANDO ANUNCIOS COM MENOS DE 7 DIAS '
    print('-' * len(titulo4))
    print(titulo4)
    print('-' * len(titulo4))
    sleep(4)
    # --------------------- MENOS DE 7 DIAS ---------------------
    for i, j in bancoFiltroDataMenor.items():
        cadastro = bancoFiltroDataMenor[i][0]
        relatorio = bancoFiltroDataMenor[i][1]
        print('\n')
        print(
            'ID Anuncio: {} | Cliente: {} | Anuncio: {} | Data de Inicio: {} | Data de Termino: {} | Investimento Inicial: R${:.2f}'.format(
                i, cadastro[1], cadastro[0], cadastro[2], cadastro[3], float(cadastro[4])))
        print('\n')
        print(
            'Investimento Total: R${:.2f} | Vizualizacoes Max.: {} | Cliques Max.: {} | Compartilhamentos Max.: {}'.format(
                float(relatorio[0]), relatorio[1], int(relatorio[2]), int(relatorio[3])))
        print('\n')
filtroCliente = input('Gostaria de filtrar os anuncios por Cliente? [S / N]:  ').lower().strip()
print("\n")
# --------------- ORDENAR OS ANUNCIOS EM ORDEM ALFABETICA COMO BASE O NOME DOS CLIENTES --------------------
titulo5 = 'LISTANDO CLIENTES EM ORDEM ALFABETICA'
print('-' * len(titulo5))
print(titulo5)
print('-' * len(titulo5))
sleep(4)
if filtroCliente == 's':
    for i in sorted(bancoFiltroCliente, key=bancoFiltroCliente.get(1)):
        a = bancoFiltroCliente[i][0]
        b = bancoFiltroCliente[i][1]
        print('\n')
        print(
            'Cliente: {} | Anuncio: {} | Data de Inicio: {} | Data de Termino: {} | Investimento Inicial: R${:.2f}'.format(
                a[1], a[0], a[2], a[3], a[4]))
        print('\n')
        print('Investimento Total: R${} | Vizualizacoes Max.: {} | Cliques Max.: {} | Compartilhamentos Max.: {}'.format(
            b[0], b[1], b[2], int(b[3])))
        print('\n')

print('\n')
wb.save(f"banco_de_dados.xlsx")
aviso1 = 'Salvando relatorio geral em uma Planilha Excel'
aviso2 = 'Acesse a pasta do programa para abrir'
print('-' * len(aviso1))
print(aviso1)
print(aviso2)
print('-' * len(aviso1))
sleep(4)


os.system("pause")
