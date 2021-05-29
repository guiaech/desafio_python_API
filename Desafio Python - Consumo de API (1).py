#!/usr/bin/env python
# coding: utf-8

# Desafio Python - Consumo de API

# In[12]:


import requests 
import json

cotacoes_bit = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR")
cotacoes_bit = cotacoes_bit.json()
cotacao_dolar= cotacoes_bit["USD"]
print(f"Valor da cotação do BTCUSD é :${cotacao_dolar}")


# In[13]:


cotacoes_eth = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,JPY,EUR")
cotacoes_eth = cotacoes_eth.json()
cotacaoeth_dolar= cotacoes_eth["USD"]
print(f"Valor da cotação do ETHUSD é :${cotacaoeth_dolar}")


# In[14]:


cotacoes_ltc = requests.get("https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,JPY,EUR")
cotacoes_ltc = cotacoes_ltc.json()
cotacaoltc_dolar= cotacoes_ltc["USD"]
print(f"Valor da cotação do LTCUSD é :${cotacaoltc_dolar}")


# In[ ]:




