'''
Autores: João Roberto Wiggert Spina e Nilton Gomes Martins Junior

Este programa é parte do projeto final da disciplina de Mineração de Dados.

Este programa interage com a API do servidor Flask, recebendo do usuário os parâmetros de um imóvel
por linha de comando, empacotando-os num JSON e enviando a mensagem para o endpoint apropriado.
O valor do imóvel é então exibido no terminal para o usuário. Os seguintes parâmetros são obrigatórios:

-Zona
-Area
-AnoConstrucao
-QualidadeAquecimento
-Banheiros
-Quartos_t1
-Quartos_t2
-Comodos
-Lareiras
-Garagem
-Qualidade

Exemplo de uso:

python predict_price.py -Zona="RL" -Area=9600 -AnoConstrucao=1976 -QualidadeAquecimento="Ex" -Banheiros=2 -Quartos_t1=3 -Quartos_t2=4 -Comodos=6 -Lareiras=1 -Garagem=2 -Qualidade=6

Obs.: A chamada para esse script só pode ser feita após a inicialização do servidor.
'''

import argparse
import json
import requests

if __name__ == "__main__":
    # Tratamento dos argumentos de entrada

    # Instância do parser
    parser = argparse.ArgumentParser(description="Regressor com Árvore de Decisão")

    # Argumentos obrigatórios
    parser.add_argument('-Zona', required=True, type=str, help='"RL" para imóveis em zonas de baixa densidade residencial;\n"RM" para imóveis em zonas de média densidade residencial')
    parser.add_argument('-Area', required=True, type=int, help='Inteiro com a área do imóvel em pés quadrados')
    parser.add_argument('-Qualidade', required=True, type=int, help='Inteiro com uma avaliação da qualidade do imóvel')
    parser.add_argument('-AnoConstrucao', required=True, type=int, help='Ano de construção do imóvel')
    parser.add_argument('-QualidadeAquecimento', required=True, type=str, help='"Ex" para excelente;\n"Gd" para bom;\n"TA" para mediano;\n"Fa" para aceitável')
    parser.add_argument('-Banheiros', required=True, type=int, help='Número de banheiros no imóvel')
    parser.add_argument('-Quartos_t1', required=True, type=int, help='Número de quartos do tipo 1 no imóvel')
    parser.add_argument('-Quartos_t2', required=True, type=int, help='Número de quartos do tipo 2 no imóvel')
    parser.add_argument('-Comodos', required=True, type=int, help='Número de cômodos no imóvel')
    parser.add_argument('-Lareiras', required=True, type=int, help='Número de lareiras no imóvel')
    parser.add_argument('-Garagem', required=True, type=int, help='Capacidade de veículos na garagem do imóvel')

    # Leitura dos argumentos
    args = parser.parse_args()

    # Definição do exemplo de entrada
    input_example = json.dumps({'Zona': args.Zona, 'Area': args.Area, 'Qualidade': args.Qualidade, 'AnoConstrucao': args.AnoConstrucao, 'QualidadeAquecimento': args.QualidadeAquecimento, 'Banheiros': args.Banheiros, 'Quartos_t1': args.Quartos_t1, 'Quartos_t2': args.Quartos_t2, 'Comodos': args.Comodos, 'Lareiras': args.Lareiras, 'Garagem': args.Garagem})
    
    # URL
    url = 'http://localhost:9000/api'

    # Resposta da API
    r = requests.post(url, input_example)

    print('Preço predito: {:.2f}'.format(r.json()['results'][0]))