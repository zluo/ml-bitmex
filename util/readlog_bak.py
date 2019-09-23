
# to see if can run Python, using print () function

# read file

import os
import pandas as pd
import json as js


print(os.getcwd())


# .  ==> current path
# .. ==> parent path

os.chdir(".\..\log")

print(os.getcwd())

# find word Ticker, Market Depth, Recent Trades
# use turple()  get mutiple result
key_words_dic = {"Instrument data:": None , "Ticker:": None, "Market Depth:": None, "Recent Trades:": None}
#key_words = ["Recent Trades:"]
# market_df = None
# recent_df = None
# ticker_df = None
# instrument_df = None

def  find_keyword(line):
    for word in key_words_dic.keys():
        if word in line:
            result = line.find(word)
            #print(result)
            data = line[(result+len(word)):].lstrip()
            if data[0]=='{':
                data = '[' + data + ']'
            # use turple()  get mutiple result
            return word, data


#def instrument_write(instrument_string):
#    print(instrument_string)


#def ticker_write(ticker_string):

#    print(ticker_string)

def json_to_dataframe (json_string, df):
    if df is None:
        # eval() is to assign strings to DataFrame
        # if md_df is none, them create it, otherwise append it to cuarrent DataFrame
        print(json_string)
        df = pd.DataFrame(eval(json_string))
        print(df)

    else:
        tmp = pd.DataFrame(eval(json_string))
        df = df.append(tmp, ignore_index= True)

    return df.drop_duplicates()

#def recent_trades_write(recent_trades_string):
#    print(recent_trades_string)

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
        key_words_dic[word] = json_to_dataframe(data, key_words_dic[word])
#        print(word, data)

 #       if word ==key_words[0]:
           # instrument_df = json_to_dataframe(data, instrument_df)
 #           pass
 #       if word ==key_words[1]:
           # json_to_dataframe(data, ticker_df)
 #          pass
 #       if word ==key_words[2]:
           #market_df = json_to_dataframe(data,market_df)
 #          pass
 #       if word == key_words[0]:
           #df = json_to_dataframe(data, key_words_dic[word])
           #key_words_dic[word] = df


 #          pass
file.close()

print(recent_df)
#print(market_df)
print(instrument_df)
print(ticker_df)

# below is printing function objects,not necessary
#print (instrument_write)
#print (ticker_write)
#print (market_depth_write)
#print (recent_trades_write)

