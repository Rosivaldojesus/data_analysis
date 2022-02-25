from tabela_empresas import fundamentos
import pandas as pd

cotacoes_df = pd.read_excel("Cotacoes.xlsx")
cotacoes = {}
for empresa in cotacoes_df["Empresa"].unique():
    cotacoes[empresa] = cotacoes_df.loc[cotacoes_df['Empresa'] == empresa, :]
print(cotacoes["ABEV3"])