'''
Autores: João Roberto Wiggert Spina e Nilton Gomes Martins Junior

Este programa é parte do projeto final da disciplina de Mineração de Dados.

Este programa implementa um servidor Flask com uma API contendo um único endpoint utilizado para realizar
a predição do preço de um imóvel com base num determinado conjunto de parâmetros do mesmo passados no corpo
da mensagem (em formato JSON).

Exemplo de uso:

python flask_server.py

Inicia o servidor, deixando-o pronto para responder requisições de predição.
'''

from flask import Flask, abort, jsonify, request
import numpy as np
from predictor import Predictor

# Modelo de regressão
model = Predictor("./decision_tree_regressor.pkl")

app = Flask(__name__)

def map_heating_quality_to_value(quality_cat):
    quality_map = {'Ex' : 4, 'Gd' : 3, 'TA' : 2, 'Fa' : 1}
    return quality_map[quality_cat]

def map_zone_to_value(zone_cat):
    zone_map = {'RL' : 1, 'RM' : 0}
    return zone_map[zone_cat]

@app.route('/api', methods=['POST'])
def make_prediction():
    # Requisita as features
    data = request.get_json(force=True)
    prediction_request = [map_zone_to_value(data['Zona']), data['Area'], data['Qualidade'], data['AnoConstrucao'], map_heating_quality_to_value(data['QualidadeAquecimento']), data['Banheiros'], data['Quartos_t1'], data['Quartos_t2'], data['Comodos'], data['Lareiras'], data['Garagem']]
    prediction = model.predict([prediction_request])
    output = [prediction[0]]
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port='9000', debug=True)