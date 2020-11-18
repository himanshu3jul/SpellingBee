# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:11:10 2020

@author: himan
"""

import numpy as np
import pandas as pd
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

master = pd.read_csv(r"C:\Users\himan\PythonProjects\SpellingBee\spellings.csv",header = 0)

column_names = ["word", "example"]

master_examples = pd.DataFrame(columns = column_names)
for index,row in master.iterrows():
    a = row['word']
    sysnets = wordnet.synsets(a)
    for s in range(len(sysnets)):
        if (a + ".") in sysnets[s].name():
            if len(wordnet.synset(sysnets[s].name()).examples()) == 0:
                continue
            else:
                for e in range(len(wordnet.synset(sysnets[s].name()).examples())):
                    if ((a+" ") in wordnet.synset(sysnets[s].name()).examples()[e]) or ((a+".") in wordnet.synset(sysnets[s].name()).examples()[e]) or ((a+",") in wordnet.synset(sysnets[s].name()).examples()[e]) or ((a+'"') in wordnet.synset(sysnets[s].name()).examples()[e]) or ((a+"?") in wordnet.synset(sysnets[s].name()).examples()[e]) or ((a+"!") in wordnet.synset(sysnets[s].name()).examples()[e]):
                        master_examples = master_examples.append({'word': a,'example': wordnet.synset(sysnets[s].name()).examples()[e]}, ignore_index=True)
                        match = 1
                        break
                    else:
                        match = 0
                        continue
                if match == 1:
                    break
                else:
                    continue
                
            
old_spellingwithexample = pd.read_csv(r"C:\Users\himan\PythonProjects\SpellingBee\spellingswithexample.csv",header = 0)

comparison_df = master_examples.merge(old_spellingwithexample,indicator=True,how='outer')

comparios_df_spelling = comparison_df[['word']].merge(master[['word']],indicator=True,how='outer')

comparios_df_filter = comparios_df_spelling[comparios_df_spelling['_merge']=="right_only"]

comparios_df_filter['example'] = ""

comparios_df_final = comparison_df[['word','example']].merge(comparios_df_filter[['word','example']],indicator=True,how='outer')

comparios_df_final[['word','example']].to_csv(r"C:\Users\himan\PythonProjects\SpellingBee\spellingswithexample.csv",mode='w', index=False)