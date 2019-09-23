import os
print(os.getcwd())

os.chdir(".\..\log")
print(os.getcwd())

keywords=["Instrument data:", "Recent Trades:", "Ticker:", "Market Depth:"]

def find_data(_keywords, _line):
    for _keyword in _keywords:
        if _keyword in _line:
            _result =_line.find(_keyword)
            _string=_line[(_result+len(_keyword)+1):]
            return _keyword, _string

# function name were actions,use verbes to give meaningful name
def get_instrument(_value):
    print(_value)

def get_recent_data(_value):
    print(_value)

def get_ticker_data(_value):
    print(_value)

def get_market_data(_value):
    print(_value)

file= open("trades.log", "r")
for line in file:
        result = find_data(keywords, line)
        if result is not None:
           key, data = result[0],result[1]
           #print(key, data)

# below codes must in this loop, as key and data was not defined outside the loop, can not be referenced
           if key==keywords[0]:
               instruement_data= get_instrument(data)
           if key==keywords[1]:
               recent_trades_data= get_recent_data(data)
           if key==keywords[2]:
               ticker_data= get_ticker_data(data)
           if key==keywords[3]:
               market_depth_data= get_market_data(data)

