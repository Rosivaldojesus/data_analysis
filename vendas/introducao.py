import pandas as pd

# Criando um dataframe a partir de um dicionário
venda = {
    'data': ['13/11/1989', '24/07/1994'],
    'valor': [500, 300],
    'produto': ['Feijão', 'Arroz'],
    'quantidade': [50, 70]

}
vendas_df = pd.DataFrame(venda)

# Visualizando o DataFrame
print(vendas_df)