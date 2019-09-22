import os
print(os.getcwd())

os.chdir(".\..\log")
print(os.getcwd())

keywords=["Instrument data:", "Recent Traders:", "Ticker:", "Market Depth:"]

def find_data(_keywords, _line):
    for _keyword in _keywords:
        if _keyword in _line:
            _result =_line.find(_keyword)
            _string=_line[(_result+len(_keyword)+1):]
            return _keyword, _string


file= open("trades.log", "r")
for line in file:
        result = find_data(keywords, line)
        if result is not None:
           key, data = result[0],result[1]
           print(key, data)

def instrument_data(_value):
    print(_value)

def Recent_data(_value):
    print(_value)

def Ticker_data(_value):
    print(_value)

def Market_data(_value):
    print(_value)


if key==keywords[0]:
    instruement_data= instrument_data(data)
if key==keywords[1]:
    recent_Traders_data= Recent_data(data)
if key==keywords[2]:
    Ticker_data= Ticker_data(data)
if key==keywords[3]:
    Market_Depth_data= Market_data(data)


