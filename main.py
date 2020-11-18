# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:22:40 2020

@author: himan
"""


from graphics import *
import math
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
from datetime import date


def isButton(p,rect):#function to check if the mouse click is in within the rectangle
    p1 = rect.getP1()
    p2 = rect.getP2()
    if(p.getX() > p1.getX() and p.getX() < p2.getX() and p.getY() > p1.getY() and p.getY() < p2.getY() ):
        return "true"
    else:
        return "false"
       
def delay(d):#function for additing delay
    for i in range(d):
        for i in range(10000):
            pass

def sayword(word):#function for saying the word
    engine = py.init()
    engine.setProperty('rate', 123)
    engine.say(word)
    engine.runAndWait()
    
def saysentence(example):#function for saying the word
    engine = py.init()
    engine.setProperty('rate', 123)
    engine.say(example)
    engine.runAndWait()
       
def main():
    master = pd.read_csv(r"C:\Users\himan\PythonProjects\SpellingBee\spellingswithexample.csv",header = 0)
    master_testscore = pd.read_csv(r"C:\Users\himan\PythonProjects\SpellingBee\testscore.csv",header = 0)

    test = master.sample(20)
    testno = master_testscore[['testno']].max().iloc[0]
    if math.isnan(testno) == True:
        testno = 1
    else:
        testno = testno + 1
    
    today = date.today()
    n = 0
    column_names = ["testno", "date","word","answer","score"]

    testscore = pd.DataFrame(columns = column_names)
    
    win = GraphWin("Spelling Bee",1000,500) #creating graphic window
    Text(Point(70,30), "Test Number: " + str(testno)).draw(win)
    Text(Point(96,50), "Test Date: " + str(today)).draw(win)
    Text(Point(58,70), "Word No: ").draw(win)
    Text(Point(420, 250), "Answer:").draw(win)

   
    answer = Entry(Point(550,250), 20)#draw entry point for Answer
    answer.setText("")
    answer.setFill("White")
    answer.draw(win)
    
    word_no = Entry(Point(110,70), 2)#draw entry point for word number
    word_no.setText("1")
    word_no.setFill("White")
    word_no.draw(win)
   
  
    WB = Rectangle(Point(130, 285),Point(270, 315)) #Word Button
    WB.setFill('yellow')
    WB.draw(win)
    WBT = Text(Point(200,300),"")#Word button
    WBT.setText("Word")
    WBT.draw(win)
    SB = Rectangle(Point(400, 285), Point(540, 315))# Sentence Button
    SB.setFill('yellow')
    SB.draw(win)
    SBT = Text(Point(470,300),"")#Sentence Button
    SBT.setText("Sentence")
    SBT.draw(win)
    NB = Rectangle(Point(670, 285), Point(810, 315))# Next Button
    NB.setFill('green')
    NB.draw(win)
    NBT = Text(Point(740,300),"")#Next Button
    NBT.setText("Next")
    NBT.draw(win)
    while True:
        p = win.getMouse()#capturing mouse click
        if(isButton(p,WB) == "true"):#if mouse is in word button
            WB.setFill('grey')
            delay(1000)
            word = test.iloc[n]['word']
            sayword(word)
            WB.setFill('yellow')
        elif(isButton(p, SB) == "true"):#if mouse is in semtemce button
            SB.setFill('grey')
            delay(1000)
            example = test.iloc[n]['example']
            saysentence(example)
            SB.setFill('yellow')
        elif(isButton(p,NB) == "true"):#if mounse is in next button
            NB.setFill('grey')
            ans = answer.getText()
            if ans == test.iloc[n]['word']:
                temp = pd.DataFrame([[testno,today,test.iloc[n]['word'],ans,1]], columns= column_names)
            else:
                temp = pd.DataFrame([[testno,today,test.iloc[n]['word'],ans,0]], columns= column_names)
            temp.to_csv(r"C:\Users\himan\PythonProjects\SpellingBee\testscore.csv", mode='a',header = False, index=False)
            if n == 19:
                break
            else:
                n = n+1
                answer.setText("")
                NB.setFill('green')
                word_no.setText(n+1)
            
    win.close()
    #win.close()
main()