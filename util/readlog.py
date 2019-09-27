
import os
import pandas as pd

os.chdir(".\..\log")
print(os.getcwd())

# set None for empty DataFrame as initial value
key_words_dic = {"Instrument data:": None , "Ticker:": None, "Market Depth:": None, "Recent Trades:": None}


def  find_keyword(line):

    for word in key_words_dic.keys():
        if word in line:
            #data = extract_json(word, line)
            #key_words_dic[word] = json_to_dataframe(data, key_words_dic[word])
# function stack trace
            key_words_dic[word] = json_to_dataframe(extract_json(word, line), key_words_dic[word])

def extract_json(word, line):
    result = line.find(word)
    data = line[(result + len(word)):].lstrip()
    if data[0]=='{':
        data = '[' + data + ']'
    return eval(data) # eval() is to assign strings to DataFrame

def json_to_dataframe (json, df):
    if df is None: # if df is none, then create a new DataFrame
        df = pd.DataFrame(json)
    else: # Dataframe has already existed, then append to existing one.
        tmp = pd.DataFrame(json)
        df = df.append(tmp, ignore_index= True)
    return df.drop_duplicates()

file = open( "trades.log", "r" )
for line in file:
    find_keyword(line)

file.close()

for key in key_words_dic:
    df = key_words_dic[key]
    print(df)
    file_name = key.replace(' ', '_')[:-1] + '.csv'
    print(file_name)
    df.to_csv(file_name, index = None, header=True)