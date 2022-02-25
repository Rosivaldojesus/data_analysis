import pandas as pd

tabela = pd.read_excel("Vendas.xlsx")

faturamento_total = tabela["Valor Final"].sum()
print(f'Faturamento total é de R$: {faturamento_total}')
