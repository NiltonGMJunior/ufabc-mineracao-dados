'''
Autores: João Roberto Wiggert Spina e Nilton Gomes Martins Junior

Este programa é parte do projeto final da disciplina de Mineração de Dados.

Este programa implementa um regressor de árvore de decisão para precificar um imóvel e retorna o modelo serializado.
O modelo é treinado com base nos dados do desafio da Keycash, baseados no dataset do Kaggle.
As características do imóvel devem ser passadas como parâmetro através do terminal/prompt de comando.

Exemplo de uso:

python serialize_model.py -random_state=33 -max_leaf_nodes=24

Gera um arquivo com nome "decision_tree_regressor.pkl" na pasta do script, contendo o modelo serializado.
'''

import numpy as np
import pandas as pd
import argparse
import pickle
from sklearn.tree import DecisionTreeRegressor

def map_heating_quality_to_value(quality_cat):
    quality_map = {'Ex' : 4, 'Gd' : 3, 'TA' : 2, 'Fa' : 1}
    return quality_map[quality_cat]

def map_zone_to_value(zone_cat):
    zone_map = {'RL' : 1, 'RM' : 0}
    return zone_map[zone_cat]

if __name__ == "__main__":
    # Tratamento dos argumentos de entrada

    # Instância do parser
    parser = argparse.ArgumentParser(description="Regressor com Árvore de Decisão")

    # Argumentos opcionais
    parser.add_argument('-random_state', required=False, type=int, help='Seed de aleatoriedade (33 por padrão)')
    parser.add_argument('-max_leaf_nodes', required=False, type=int, help='Número máximo de nós na árvore (24 por padrão)')

    # Leitura dos argumentos
    args = parser.parse_args()
    
    # Caminho para o conjunto de dados
    data_path = "./dados.csv"

    # Criação do dataframe
    df = pd.read_csv(data_path, sep=';', index_col='Id')
    df['QualidadeAquecimento'] = df['QualidadeAquecimento'].apply(map_heating_quality_to_value)
    df['Zona'] = df['Zona'].apply(map_zone_to_value)

    # Denominação das colunas de features e labels
    features = ['Zona', 'Area', 'Qualidade', 'AnoConstrucao', 'QualidadeAquecimento', 'Banheiros', 'Quartos_t1', 'Quartos_t2', 'Comodos', 'Lareiras', 'Garagem']
    labels = ['Preco']

    # Determinação do conjunto de features e labels
    X = df[features]
    y = df[labels]

    # Criação do modelo de regressão
    model = DecisionTreeRegressor(max_leaf_nodes=(1000 if not args.max_leaf_nodes else args.max_leaf_nodes), random_state=(33 if not args.random_state else args.random_state))
    model.fit(X, y)

    with open('decision_tree_regressor.pkl', 'wb') as handle:
        pickle.dump(model, handle, pickle.HIGHEST_PROTOCOL)