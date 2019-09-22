import os
os.chdir(".\..\log")
print (os.getcwd())

file = open ("trades.log","r")
#for line in file:
    #print(line)


def get_key_data(_key, _line):
    for _keyword in _key:
        if _keyword in _line:
            _position=_line.find(_keyword)
            _result=_line[(_position+ len(_keyword)+1):]
            return (_keyword, _result)

keywords = ["Instrument data:","Ticker:", "Market Depth:", "Recent Trades:"]
for line in file:
    result= get_key_data(keywords, line)
    if result != None:
        key,value = result
        print(key, value)