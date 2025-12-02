import requests

response = requests.get('https://api.adviceslip.com/advice') # Vai no site e pegar as informações

print(response.status_code) # Verifica se o site está tudo funcionando. Deve-se retornar um valor.
print(response.json()) # Mostra o conteúdo do site 
print(response.json()['slip']) # Mostra o conteúdo da chave 'slip'
print(response.json()['slip']['id']) # Dentro da chave 'slip' pega o conteúdo da chave 'id'
print(response.json()['slip']['advice']) # Dentro da chave 'slip' pega o conteúdo da chave 'advice'