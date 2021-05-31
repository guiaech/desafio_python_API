import os
import time
import json
import requests


while x (True):
    cotacoes_bit = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR")
    cotacoes_bit = cotacoes_bit.json()
    cotacao_dolar = cotacoes_bit["USD"]
    print(f"Valor da cotação do BTCUSD é :${cotacao_dolar}")

    cotacoes_eth = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,JPY,EUR")
    cotacoes_eth = cotacoes_eth.json()
    cotacaoeth_dolar = cotacoes_eth["USD"]
    print(f"Valor da cotação do ETHUSD é :${cotacaoeth_dolar}")

    cotacoes_ltc = requests.get("https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,JPY,EUR")
    cotacoes_ltc = cotacoes_ltc.json()
    cotacaoltc_dolar = cotacoes_ltc["USD"]
    print(f"Valor da cotação do LTCUSD é :${cotacaoltc_dolar}")

    time.sleep(30)
        if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
