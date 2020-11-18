# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:39:18 2020

@author: himan
"""


import numpy as np
import pandas as pd
import pronouncing as pr
import pyttsx3 as py
from PyDictionary import PyDictionary
from vocabulary.vocabulary import Vocabulary as vb
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from csv import writer
import date

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

master = pd.read_csv(r"C:\Users\himan\PythonProjects\SpellingBee\spellingswithexample.csv",header = 0)
master_testscore = pd.read_csv(r"C:\Users\himan\PythonProjects\SpellingBee\testscore.csv",header = 0)

test = master.sample(20)
testno = master_testscore[['testno']].max().fillna(0) + 1
today = date.today()

column_names = ["testno", "date","word","answer","score"]

testscore = pd.DataFrame(columns = column_names)

engine = py.init()
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 123)



for index,row in master.iterrows():
    engine.say(row['word'])
    engine.runAndWait()
    engine.say(row['example'])
    engine.runAndWait()
  
# dictionary=PyDictionary()
# a = dictionary.meaning("just")
# print(vb.usage_example("just",format="dict"))
# #engine.say(vb.usage_example("just"))
# #engine.runAndWait()
# a = wordnet.synsets('program')
# print(a)
# result = []
# for s in range(len(a)):
#     print(a[s].name())
#     if 'program.' in a[s].name():
#         result.append(a[s])
#         break

# print(result)
# print(wordnet.synset('program.n.02').examples()[0])