import pandas as pd

# Importando uma base de dados
vendas_df = pd.read_excel("Vendas.xlsx")
print(vendas_df.head(10))