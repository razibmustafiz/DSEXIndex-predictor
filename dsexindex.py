
# This is a Python program to predict Dhaka Stock Exchange(DSEX) Index price
# in two days advance using AI with Quantile Regression Algorithm. Developed by Razib Mustafiz. razib.mustafiz@gmail.com
# Version no 1.00  



print("Dhaka Stock Exchange(DSEX)Index price predictor for two days advance by NRB Finance LTD.© NRBFL 2020.All Rights reserved.V 1.00")

import urllib.request
import json


x_datetime = (input("Enter Date YYYY-MM-DD:"))
x_Change = (input("Enter Change:"))
x_Volume = (input("Enter Volume:"))
x_Volspikepercent = (input("Enter Volume Spike %:"))
x_ofAvgVolpercent = (input("Enter % of AVG VOL :"))
x_5DAVGVOL = (input("Enter 5 Day Average Volume:"))
x_21DAVGVOL = (input("Enter 21 Day Average Volume:"))
x_50DAVGVOL = (input("Enter 50 Day Average Volume:"))
x_RSI50 = (input("Enter RSI 50:"))
x_ADX = (input("Enter ADX:"))
x_plusDI = (input("Enter DI+:"))
x_minusDI = (input("Enter DI-:"))
x_ADXChange = (input("Enter ADXChange:"))
x_SAR = (input("Enter SAR:"))
x_MACD = (input("Enter MACD:"))
x_Signal = (input("Enter Signal:"))
x_RSI = (input("Enter RSI:"))
x_ROC15 = (input("Enter ROC 15:"))
x_MFI = (input("Enter MFI:"))
x_OBV = (input("Enter OBV:"))
x_CCI = (input("Enter CCI:"))
x_Ultimate = (input("Enter Ultimate:"))
x_EMA5 = (input("Enter EMA-5:"))
x_EMA10 = (input("Enter EMA-10:"))
x_EMA20 = (input("Enter EMA-20:"))
x_EMA50 = (input("Enter EMA-50:"))
x_EMA120 = (input("Enter EMA-120:"))
x_WMA5 = (input("Enter WMA-5:"))
x_WMA10 = (input("Enter WMA-10:"))
x_WMA20 = (input("Enter WMA-20:"))
x_WMA50 = (input("Enter WMA-50:"))
x_WMA120 = (input("Enter WMA-120:"))
x_WMA2000 = (input("Enter WMA-2000:"))
x_StochasticpercentK = (input("Enter Stochastic %K:"))
x_StochasticpercentD = (input("Enter Stochastic %D:"))
x_AroonDown = (input("Enter Aroon Down:"))
x_AroonUp = (input("Enter Aroon UP:"))
x_AroonOsc = (input("Enter Aroon Osc:"))
x_BollingerTop = (input("Enter Bollinger Top:"))
x_BollingerBot = (input("Enter Bollinger Bot:"))
x_Squeeze = (input("Enter Squeeze:"))
x_RMI = (input("Enter RMI:"))
x_Open = (input("Enter Open:"))
x_High = (input("Enter High:"))
x_Low = (input("Enter Low:"))
x_Close = (input("Enter Close:"))


data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Ticker': "00DSEX",   
                            'Date/Time': (x_datetime),   
                            'Change': (x_Change),   
                            'Volome': (x_Volume),   
                            'VolSpike %': (x_Volspikepercent),   
                            '% Of Avg Vol': (x_ofAvgVolpercent),   
                            '5 D AVG VOL': (x_5DAVGVOL),   
                            '21 D AVG VOL': (x_21DAVGVOL),   
                            '50 D AVG VOL': (x_50DAVGVOL),   
                            'RSI 50': (x_RSI50),   
                            'ADX': (x_ADX),   
                            'DI+': (x_plusDI),   
                            'DI-': (x_minusDI),   
                            'ADXChange': (x_ADXChange),   
                            'SAR': (x_SAR),   
                            'MACD': (x_MACD),   
                            'Signal': (x_Signal),   
                            'RSI': (x_RSI),   
                            'ROC(15)': (x_ROC15),   
                            'MFI': (x_MFI),   
                            'OBV': (x_OBV),   
                            'CCI': (x_CCI),   
                            'Ultimate': (x_Ultimate),   
                            'EMA-5': (x_EMA5),   
                            'EMA-10': (x_EMA10),   
                            'EMA-20': (x_EMA20),   
                            'EMA-50': (x_EMA50),   
                            'EMA-120': (x_EMA120),   
                            'WMA-5': (x_WMA5),   
                            'WMA-10': (x_WMA10),   
                            'WMA-20': (x_WMA20),   
                            'WMA-50': (x_WMA50),   
                            'WMA-120': (x_WMA120),   
                            'WMA-2000': (x_WMA2000),   
                            'Stochastic %K': (x_StochasticpercentK),   
                            'Stochastic %D': (x_StochasticpercentD),   
                            'Aroon_Down': (x_AroonDown),   
                            'Aroon_Up': (x_AroonUp),   
                            'Aroon_Osc': (x_AroonOsc),   
                            'BollingerTop': (x_BollingerTop),   
                            'BollingerBot': (x_BollingerBot),   
                            'Squeeze': (x_Squeeze),   
                            'RMI': (x_RMI),   
                            'Open': (x_Open),   
                            'High': (x_High),   
                            'Low': (x_Low),   
                            'Close': (x_Close),   
                            'Close(5)': "1857",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/891285f9f40b45f793345ab13678b7b2/services/9bcd6cedb24e4a1e92db0757e9c73a4c/execute?api-version=2.0&format=swagger'
api_key = 'cnhXZGwEFA59JskMOn2CS47UKet7tPeTbPaPCMOXEAfqpu4k125mHGE7ihaH64lPmjxhTW0H/Cgmzvrf5KSPpA=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))