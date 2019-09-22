print("hello")
# to see if can run Python, using print () function

# read file

import os
print(os.getcwd())

# .  ==> current path
# .. ==> parent path

os.chdir(".\..\log")

print(os.getcwd())

# find word Ticker, Market Depth, Recent Trades
# use turple()  get mutiple result
key_words = ["Instrument data:","Ticker:", "Market Depth:", "Recent Trades:"]
def  find_keyword(line):
    for word in key_words:
        if word in line:
            result = line.find(word)
            #print(result)
            data_keyword= line[(result+len(word)):]

            # use turple()  get mutiple result
            return word, data_keyword.lstrip()


def instrument_write(instrument_string):
    print(instrument_string)


def ticker_write(ticker_string):
    print(ticker_string)

def maket_depth_write(maket_depth_string):
    print(maket_depth_string)

def recent_trades_write(recent_trades_string):
    print(recent_trades_string)

# open file
# result=text.find("")  to determine position
# use function in loop to get result
file = open( "trades.log", "r" )
for line in file:
    #print(line, end="")
    result = find_keyword(line)
    if result is not None:
        #print(result)
        word, data = result
        #print(word, data)

        if word ==key_words[0]:
            instrument_write(data)
        if word ==key_words[1]:
            ticker_write(data)
        if word ==key_words[2]:
            maket_depth_write(data)
        if word ==key_words[3]:
            recent_trades_write(data)










