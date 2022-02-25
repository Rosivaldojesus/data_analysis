import pandas as pd
import os

empresas = ['ABEV3', 'AZUL4']

fundamentos = {}
arquivos = os.listdir("balancos")
for arquivo in arquivos:
    nome = arquivo[-9:-4]
    if "11" in nome:
        nome = arquivo[-10: -4]
    if nome in empresas:
        # Pegar o balanço daquela empresa
        # O sheet_name pega a aba da planilha
        # Pegando a aba 1 do arquivo excel
        balanco = pd.read_excel(f'balancos/{arquivo}', sheet_name=0)

        # Na primeira coluna colocar o título com o nome da empresa
        balanco.iloc[0, 0] = nome

        # Pegou a 1ª linha e tornou um cabeçalho
        balanco.columns = balanco.iloc[0]
        balanco = balanco[1:]

        # Coloca o nome da coluna em uma linha e o nome da empresa em outra linha
        balanco = balanco.set_index(nome)
        # ================================================================================
        # Pegando a aba 2 do arquivo excel
        dre = pd.read_excel(f'balancos/{arquivo}', sheet_name=1)

        # Na primeira coluna colocar o título com o nome da empresa
        dre.iloc[0, 0] = nome

        # Pegou a 1ª linha e tornou um cabeçalho
        dre.columns = dre.iloc[0]
        dre = dre[1:]

        # Coloca o nome da coluna em uma linha e o nome da empresa em outra linha
        dre = dre.set_index(nome)

        fundamentos[nome] = balanco.append(dre)
        print(fundamentos)
        #print(balanco)
        #print(dre)


