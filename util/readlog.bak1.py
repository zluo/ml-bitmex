
import os
import pandas as pd

os.chdir(".\..\log")
print(os.getcwd())

# set None for empty DataFrame as initial value
key_words_dic = {"Instrument data:": None , "Ticker:": None, "Market Depth:": None, "Recent Trades:": None}


def  find_keyword(line1):

    for word1 in key_words_dic.keys():
        if word1 in line1:
            #data1 = extract_json(word1, line1)
            #key_words_dic[word1] = json_to_dataframe(data1, key_words_dic[word1])

            key_words_dic[word1] = json_to_dataframe(extract_json(word1, line1), key_words_dic[word1])

def extract_json(word2, line2):
    result = line2.find(word2)
    data2 = line2[(result+len(word2)):].lstrip()
    if data2[0]=='{':
        data2 = '[' + data2 + ']'
    return data2

def json_to_dataframe (json_string, df):
    if df is None:
        # eval() is to assign strings to DataFrame
        # if md_df is none, them create it, otherwise append it to cuarrent DataFrame
        #print(json_string)
        df = pd.DataFrame(eval(json_string))
        #print(df)
    else:
        tmp = pd.DataFrame(eval(json_string))
        df = df.append(tmp, ignore_index= True)
    return df.drop_duplicates()

file = open( "trades.log", "r" )
for line in file:
    find_keyword(line)

file.close()

# Write dataFrame to csv files
for key in key_words_dic:
    df = key_words_dic[key]
 #   df.to_csv(key + '.csv')