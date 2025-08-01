import pandas as pd
import random
from datetime import datetime, timedelta


def gerar_estados(tam_base): 
    estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
               'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 
               'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    
    #Retorno com uma escolha random dentro da Lista e seguindo o tamanho da 'tam_base'
    return random.choices(estados, k=tam_base)


def gerar_canais_vendas(tam_base): 
    canais = ['Online', 'Loja Física']
    
    #Retorno com uma escolha random dentro da Lista e seguindo o tamanho da 'tam_base'
    return random.choices(canais, k=tam_base)


def gerar_motivo_compra(tam_base): 
    motivo_compra = ['Necessidade', 'Indicação', 'Anúncio', 'Redes Sociais']
    
    #Retorno com uma escolha random dentro da Lista e seguindo o tamanho da 'tam_base'
    return random.choices(motivo_compra, k=tam_base)


def gerar_produtos(tam_base): 
    produtos = ['Produto A', 'Produto B', 'Produto C', 
                'Produto D', 'Produto E', 'Produto F']
    
    #Retorno com uma escolha random dentro da Lista e seguindo o tamanho da 'tam_base'
    return random.choices(produtos, k=tam_base)


def gerar_valor_produtos(tam_base):
    
    #Retorno com uma escolha random dentro do range e seguindo o tamanho da 'tam_base'
    return random.choices(range(150, 351), k=tam_base)


def gerar_qtd_vendida(tam_base):
    
    #Retorno com uma escolha random dentro do range e seguindo o tamanho da 'tam_base'
    return random.choices(range(1, 21), k=tam_base)


def gerar_datas(data_inicial, data_final, tam_base):
    
    #Formato da data
    formato_data = "%d/%m/%Y"
    
    #Converter as datas inicial e final de string para objeto 'datetime'
    data_inicial = datetime.strptime(data_inicial, formato_data)
    data_final = datetime.strptime(data_final, formato_data)
    
    #Uma base de datas é gerada dentro do range e convertida para o formato_data. O tolist
    #converte o objeto para uma lista de string de datas
    base_datas = pd.date_range(data_inicial, data_final).strftime(formato_data).tolist()
    
    #rand_datas recebe as datas aleatóras dentro da base_datas e a quantidade definida pelo tam_base
    rand_datas = random.choices(base_datas, k=tam_base)
    
    #Retorno da base das datas aleatórias
    return rand_datas


def gerar_faturamento(dataframe):
    #Cálculo do faturamento e atribuindo na coluna de Faturamento
    dataframe['Faturamento'] = dataframe['Valor do Produto'] * dataframe['Quantidade Vendida']
    
    #Retorno do dataframe
    return dataframe


#Definição do tamanho da Base
qte_linhas = 20

#Definindo dataframe vazio 
dataframe = pd.DataFrame()

#Preenchendo as colunas chamando as funções
dataframe['Estado'] = gerar_estados(qte_linhas)
dataframe['Canal de Vendas'] = gerar_canais_vendas(qte_linhas)
dataframe['Motivo da Compra'] = gerar_motivo_compra(qte_linhas)
dataframe['Nome do Produto'] = gerar_produtos(qte_linhas)
dataframe['Valor do Produto'] = gerar_valor_produtos(qte_linhas)
dataframe['Quantidade Vendida'] = gerar_qtd_vendida(qte_linhas)
dataframe['Data da Venda'] = gerar_datas('01/01/2023', '30/06/2023', qte_linhas)
gerar_faturamento(dataframe)

#Exportando para Excel excluindo a coluna de índice
#dataframe.to_excel('Planilha 1.xlsx', index=False)

#Print do dataframe
print(dataframe)
