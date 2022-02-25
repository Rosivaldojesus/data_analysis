import pandas as pd

tabela = pd.read_excel("Vendas.xlsx")

faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_por_produto)