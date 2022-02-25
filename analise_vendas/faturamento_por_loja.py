import pandas as pd

tabela = pd.read_excel("Vendas.xlsx")
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)
