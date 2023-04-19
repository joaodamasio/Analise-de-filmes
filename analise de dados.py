#Analisando as notas no geral

import matplotlib.pyplot as plt
import pandas as pd

#Lendo o arquivo 
notas = pd.read_csv('ratings.csv')

#Renomeando o nome das colunas
notas.columns = ['usuariosID', 'filmeID','nota', 'momento']

#Exibindo a maior e menor nota de acordo com a quatidade de votos
notas['nota'].value_counts()

#Media geral
notas['nota'].mean()

#Olhando os filmes
filmes = pd.read_csv('movies.csv')
filmes.columns = ['filmeId', 'titulo', 'genero']

#Analisando algumas notas em especifico por filme
notas.query('filmeID==1').nota.mean()

#Agrupando os dados por filme e exibindo a nota media
media_por_filme = notas.groupby('filmeID').mean()[['nota']]
media_por_filme.head()

print(plt.hist(media_por_filme))