import requests
import json
import matplotlib.pyplot as plt
#conversor de moedas
#resumo das moedas

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL')
cotacoes_dic = cotacoes.json()
dolar2casas = float(cotacoes_dic['USDBRL']['bid'])
euro2casas = float(cotacoes_dic['EURBRL']['bid'])
btc2casas = float(cotacoes_dic['BTCBRL']['bid'])
eth2casas = float(cotacoes_dic['ETHBRL']['bid'])


print('-='*10, end = ' ')
print('Esta é a cotação das moedas para o REAL (BRL)', end = ' ')
print('-='*10)
print('Dólar: R${:.2f}'.format(dolar2casas))
print('Euro: R${:.2f}'.format(euro2casas))
print('Bitcoin: R${:.2f}'.format(btc2casas))
print('Ethereum: R${:.2f}'.format(eth2casas))
print('\n')

a = input('Deseja saber mais sobre alguma moeda? Caso sim, digite [S], caso não, digite [N]: ').strip().upper()

if a == 'S':
    print('Dólar: [1] \nEuro: [2] \nBitcoin: [3] \nEthereum: [4] \n')
    b = input('Digite sobre qual moeda você deseja saber mais: ').strip()
    if b == '1':     #usd
        dolar15 = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/15')
        dolar15dic = dolar15.json()
        lista15dolar = ['{} dias atrás Dólar: R${:.2f}'.format(dia, float(item['bid'])) for dia, item in zip(range(1, 16), dolar15dic)]

        dolarano = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/365')
        dolaranodic = dolarano.json()
        valor1ano = float(dolaranodic[359]['bid'])

        maxdolar2casa = float(cotacoes_dic['USDBRL']['high'])
        mindolar2casa = float(cotacoes_dic['USDBRL']['low'])

        dolar30 = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
        dolar30dic = dolar30.json()
        cotacaolist = [float(item['bid']) for item in dolar30dic]
        cotacaolist.reverse()      

        print('\n')
        print('Mínima de hoje: R${:.2f} '.format(mindolar2casa))
        print('Máxima de hoje: R${:.2f} '.format(maxdolar2casa))
        print('\n')
        print('Todas as cotações nos últimos 15 dias: {}'.format(lista15dolar))
        print('\n')
        print('Um ano atrás, o dólar estava: R${:.2f}'.format(valor1ano))
        print('\n')
        print('O gráfico relacionado ao Dólar de 30 dias atrás até agora: ')
        plt.figure(figsize=(15, 8))
        plt.plot(cotacaolist)
        plt.show()

    elif b == '2':  #eur
        eur15 = requests.get('https://economia.awesomeapi.com.br/json/daily/EUR-BRL/15')
        eur15dic = eur15.json()
        lista15eur = ['{} dias atrás Euro: R${:.2f}'.format(dia, float(item['bid'])) for dia, item in zip(range(1, 16), eur15dic)]

        eurano = requests.get('https://economia.awesomeapi.com.br/json/daily/EUR-BRL/365')
        euranodic = eurano.json()
        eur1ano = float(euranodic[359]['bid'])

        maxeur2casa = float(cotacoes_dic['EURBRL']['high'])
        mineur2casa = float(cotacoes_dic['EURBRL']['low'])

        eur30 = requests.get('https://economia.awesomeapi.com.br/json/daily/EUR-BRL/30')
        eur30dic = eur30.json()
        cotacaoeurlist = [float(item['bid']) for item in eur30dic]
        cotacaoeurlist.reverse()   

        print('\n')
        print('Mínima de hoje: R${:.2f} '.format(mineur2casa))
        print('Máxima de hoje: R${:.2f} '.format(maxeur2casa))
        print('\n')
        print('Todas as cotações nos últimos 15 dias: {}'.format(lista15eur))
        print('\n')
        print('Um ano atrás, o Euro estava: R${:.2f}'.format(eur1ano))
        print('\n')
        print('O gráfico relacionado ao Euro de 30 dias atrás até agora: ')
        plt.figure(figsize=(15, 8))
        plt.plot(cotacaoeurlist)
        plt.show()

    elif b == '3':  #btc
        btc15 = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/15')
        btc15dic = btc15.json()
        lista15btc = ['{} dias atrás Bitcoin: R${:.2f}'.format(dia, float(item['bid'])) for dia, item in zip(range(1, 16), btc15dic)]

        btcano = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/365')
        btcanodic = btcano.json()
        btc1ano = float(btcanodic[359]['bid'])

        maxbtc2casa = float(cotacoes_dic['BTCBRL']['high'])
        minbtc2casa = float(cotacoes_dic['BTCBRL']['low'])

        btc30 = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/30')
        btc30dic = btc30.json()
        cotacaobtclist = [float(item['bid']) for item in btc30dic]
        cotacaobtclist.reverse()       

        print('Mínima de hoje: R${:.2f} '.format(minbtc2casa))
        print('Máxima de hoje: R${:.2f} '.format(maxbtc2casa))
        print('\n')
        print('Todas as cotações nos últimos 15 dias: {}'.format(lista15btc))
        print('\n')
        print('Um ano atrás, a Bitcoin estava: R${:.2f}'.format(btc1ano))
        print('\n')
        print('O gráfico relacionado a Bitcoin de 30 dias atrás até agora: ')
        plt.figure(figsize=(15, 8))
        plt.plot(cotacaobtclist)
        plt.show()

    elif b == '4':  #eth
        eth15 = requests.get('https://economia.awesomeapi.com.br/json/daily/ETH-BRL/15')
        eth15dic = eth15.json()
        lista15eth = ['{} dias atrás Ethereum: R${:.2f}'.format(dia, float(item['bid'])) for dia, item in zip(range(1, 16), eth15dic)]

        ethano = requests.get('https://economia.awesomeapi.com.br/json/daily/ETH-BRL/365')
        ethanodic = ethano.json()
        eth1ano = float(ethanodic[359]['bid'])

        maxeth2casa = float(cotacoes_dic['ETHBRL']['high'])
        mineth2casa = float(cotacoes_dic['ETHBRL']['low'])

        eth30 = requests.get('https://economia.awesomeapi.com.br/json/daily/ETH-BRL/30')
        eth30dic = eth30.json()
        cotacaoethlist = [float(item['bid']) for item in eth30dic]
        cotacaoethlist.reverse()       

        print('Mínima de hoje: R${:.2f} '.format(mineth2casa))
        print('Máxima de hoje: R${:.2f} '.format(maxeth2casa))
        print('\n')
        print('Todas as cotações nos últimos 15 dias: {}'.format(lista15eth))
        print('\n')
        print('Um ano atrás, a Ethereum estava: R${:.2f}'.format(eth1ano))
        print('\n')
        print('O gráfico relacionado a Ethereum de 30 dias atrás até agora: ')
        plt.figure(figsize=(15, 8))
        plt.plot(cotacaoethlist)
        plt.show()
     
else:
    print('Encerrando programa.')