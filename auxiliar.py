import requests
import json



dolar15 = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/15')
dolar30 = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
dolarano = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/365')

dolar15dic = dolar15.json()
dolar30dic = dolar30.json()
dolaranodic = dolarano.json()

lista_formatada = ['Dia {}: Dólar: R${:.2f}'.format(dia, float(item['bid'])) for dia, item in zip(range(1, 16), dolar15dic)]



primeira_ocorrencia_bid = dolaranodic[359]['bid']
print(lista_formatada)