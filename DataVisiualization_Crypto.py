# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:04:00 2021

@author: Martin Chareton
"""
import cryptocompare
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import seaborn as sns
import datetime as datetime
#from datetime import datetime as dt

# Use white grid plot background from seaborn
#sns.set(font_scale=1.5, style="whitegrid")
sns.set_style("whitegrid")

#Enregistre un graphique d'évolution du prix d'une cryptomonnaie dans une devise donnée jusqu'à 2000 jours avant la date d'exécution, pour une échelle de temps donnée
def graph_save(symbol, fiat, days, scale, date, endtitle):
    #récupérer les x derniers prix journaliers de Bitcoin à partir d'aujourd'hui
    BTC_prices = cryptocompare.get_historical_price_day(symbol, fiat, limit=days, exchange='CCCAGG', toTs=datetime.datetime.today())

    #Créer un DF qui insère la date et les prix à la fermeture
    c = []
    for m in BTC_prices:
        c.append((m["time"], m["close"]))
    dfb = pd.DataFrame(c, columns=["time", "prices"])
    
    #transformer le timestamp en date dans la colonne time du dateframe
    dfb["time"] = dfb["time"].apply(datetime.date.fromtimestamp)
    
    #plot data
    fig, ax = plt.subplots()
    ax.plot('time', 'prices', data=dfb, color='tab:red')
    fig.suptitle('Evolution du prix '+endtitle, fontsize=15)
    
    #format time
    years = mdates.YearLocator()
    years_fmt = mdates.DateFormatter('%Y')
    months = mdates.MonthLocator()
    months_fmt = mdates.DateFormatter('%m-%Y')
    
    scale = scale
    if scale == 'year':
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(years_fmt)
    elif scale == 'month':
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(months_fmt)
    
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    fig.autofmt_xdate()
    fig.savefig('C:/Users/Martin Chareton/Documents/Banque de France/Pro/'+date+'_'+symbol+'_'+scale+'.jpg')

#Plot without saving
def graph(symbol, fiat, days, scale, endtitle):
    #récupérer les x derniers prix journaliers de Bitcoin à partir d'aujourd'hui
    BTC_prices = cryptocompare.get_historical_price_day(symbol, fiat, limit=days, exchange='CCCAGG', toTs=datetime.datetime.today())

    #Créer un DF qui insère la date et les prix à la fermeture
    c = []
    for m in BTC_prices:
        c.append((m["time"], m["close"]))
    dfb = pd.DataFrame(c, columns=["time", "prices"])
    
    #transformer le timestamp en date dans la colonne time du dateframe
    dfb["time"] = dfb["time"].apply(datetime.date.fromtimestamp)
    
    
    #plot data
    fig, ax = plt.subplots()
    ax.plot('time', 'prices', data=dfb, color='tab:red')
    fig.suptitle('Evolution du prix '+endtitle, fontsize=15)
    
    #format time
    years = mdates.YearLocator()
    years_fmt = mdates.DateFormatter('%Y')
    months = mdates.MonthLocator()
    months_fmt = mdates.DateFormatter('%m-%Y')
    
    scale = scale
    if scale == 'year':
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(years_fmt)
    elif scale == 'month':
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(months_fmt)
    
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    fig.autofmt_xdate()
    #fig.savefig('C:/Users/Martin Chareton/Documents/Banque de France/Pro/'+date+'_'+symbol+'_'+scale+'.jpg')
    
graph_save('BTC', 'USD', 2000, 'year', '08012020', 'du Bitcoin (USD) depuis 2016')
graph_save('BTC', 'USD', 90, 'month', '08012020', 'du Bitcoin (USD) sur 90 jours')

graph('ETH', 'USD', 1400, 'year', "de l'Ether (USD) sur quatre ans")

graph('BTC', 'USD', 90, 'month', 'du Bitcoin (USD) sur 90 jours')