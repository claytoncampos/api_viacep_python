import requests
import os

os.system('clear')

cep = input('Digite o CEP: ')
response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

data =  response.json()

print('Dados abaixo:')
print()
print('CEP: {}'.format(data['cep']))
print('Logradouro: {}'.format(data['logradouro']))
print('Bairro: {}'.format(data['bairro']))
print('Localidade: {}'.format(data['localidade']))
print('UF: {}'.format(data['uf']))