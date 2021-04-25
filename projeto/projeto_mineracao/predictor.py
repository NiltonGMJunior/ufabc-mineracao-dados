'''
Autores: João Roberto Wiggert Spina e Nilton Gomes Martins Junior

Este programa é parte do projeto final da disciplina de Mineração de Dados.

Este programa implementa um preditor com base num regressor de árvore de decisão previamente serializado.
Esta classe é utilizada no servidor Flask para gerar os resultados da API.
'''

import pickle

class Predictor():

    def __init__(self, path_to_model):
        self.model = self.deserialize(path_to_model)

    @staticmethod
    def deserialize(path_to_model):
        # Deserialização do modelo
        with open(path_to_model, 'rb') as handle:
            model = pickle.load(handle)
        return model

    def predict(self, example):
        return self.model.predict(example)