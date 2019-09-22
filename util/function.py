
def add(param1, param2):
    result = param1 + param2
    return result


a = add(5,7)

print(a)


import os
print(os.getcwd())

os.chdir(".\..\log")
print(os.getcwd())
file = open("trades.log", "r")
"""for line in file:
    print (line)"""

keywords = ["Instrument data:","Ticker:", "Market Depth:", "Recent Trades:"]

def get_value(_keys, _line):
    for _keyword in _keys:
        if _keyword in _line:
            _position=_line.find(_keyword)
            _result=_line[(_position + len(_keyword)+1):]
            return (_keyword, _result)

for line in file:
    result = get_value(keywords, line)
    #print(result)
    if result != None:
        keyword, data = result
        print(keyword, data)


def instrument_value(_value):
    print(_value)

def recent_value(_value):
    print(_value)

def market_value(_value):
    print(_value)

def ticker_value(_value):
    print(_value)


if keyword == keywords[0]:
    instrument_value = instrument_value(data):





