import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Analisando todos os dados
tmdb = pd.read_csv('tmdb_5000_movies.csv')

#Analisando em qual lingua form exibida os filmes
contagem_de_lingua=tmdb['original_language'].value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ['original_language', 'total']
contagem_de_lingua.head()

#Vizualização geral
#sns.catplot(data=tmdb, x= 'original_language',kind='count')

total_por_lingua = tmdb['original_language'].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles

dados = {
    'lingua' : ['ingles','outros'],
    'total' : [total_de_ingles, total_do_resto]
}

dados = pd.DataFrame(dados)

#Visualizando a comparação do ingles com as outras linguas
#sns.barplot(data= dados, x='lingua', y='total')

total_de_lingua_por_outros_filmes= tmdb.query('original_language != "en"').original_language.value_counts()
filmes_sem_lingua_em_ingles = tmdb.query('original_language != "en"')

#Visualizando a comparação entre as outras linguas
sns.catplot(data=filmes_sem_lingua_em_ingles, x= 'original_language',kind='count', aspect= 2, palette='GnBu_d', order= total_de_lingua_por_outros_filmes.index)

