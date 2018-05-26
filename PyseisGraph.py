# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:31:36 2018

@author: ANDY
"""

#from fftgraph import FftGraph
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib

data=pd.read_csv(r'C:\Users\ANDY\Desktop\L02072.csv')
time=[]
step=1

for i in data['Time(ms)']:
    time.append(i)
del data['Time(ms)']
          
hit_fore=True
hit_back=True
hit_show=False
hit_elong=True
hit_short=True
hit_switch=True

class VibraGraph:
    
    
    def __init__(self):
        self.times=np.linspace(1,3000,1024)
        self.fig,self.ax=plt.subplots()
        
#    step,number=2048,number*step+1 
    
    def _xvibra(self,raw_data,column):
        xvibra=[]
        testdata2=raw_data(str(column))
        for i in range(1023):
            xvibra.append(testdata2[i])
            xvibra.append((testdata2[i]+testdata2[i+1])/2)
        xvibra.append(testdata2[1023])
        
        return xvibra
    
    def minor_xvibra(self):
        pass
    
        
    def plotvibra(self,xvibra):
        self.ax.plot(xvibra,self.times,'k')
        
    def fillblank(self,xvibra,offset):
        self.ax.fill_betweenx(self.times,offset,xvibra,where=(xvibra>offset),color='k')
        
    def set_xvibralim(self,left,right):
        self.ax.set_xlim(left,right)
        
    def showImg():
        
#   clear the former image
        offset=100

       
        for i in range(1,81):
            testdata1=pd.to_numeric(data[str(i)])+offset
            self.plotvibra(testdata1)
            self.fillblank(testdata1,offset)
            offset=offset+1500
    
    
class hit_condition:
    
    
    def hit_foremove(self):
        global hit_fore
        x=VibraGraph()
        if hit_fore == True:
            hit_fore=False
            x.add_xvibra
        else:
             hit_fore=True

    def hit_backmove(self):
        global hit_back
        x=VibraGraph()
        if hit_back == True:
            hit_back=False
            
        else:
             hit_back=True

    def hit_elongate(self):
        global hit_elong,step
        x=VibraGraph()
        if hit_elong == True:
            x=VibraGraph()
            x.showImg()
            hit_elong=False
        else:
             hit_elong=True

    def hit_shorten(self):
        global hit_short,step
        x=VibraGraph()
        if hit_short == True:
            if step>1:
                step-=1
                x.showImg()
            
        else:
             hit_short=True
             

    def hit_switchimg(self):
        global hit_switch
        if hit_switch == True:
            hit_switch=False
        else:
             hit_switch=True
             
             
        
     
if __name__=='__main__':
    
    matplotlib.use('TkAgg')
    hit=hit_condition()
    x=VibraGraph()
    x.showImg()
    
#    initialize window
    window=tk.Tk()
    window.title('vibrationgraphtest')
    
    step_var=tk.IntVar()
    
    frame=tk.Frame(window)
    frame.pack()
    
    frame_left=tk.Frame(frame)
    frame_right=tk.Frame(frame)
    frame_left.pack(side='left')
    frame_right.pack(side='right')
    
    entry_elong=tk.Entry(frame_right,text=step_var)
    
    
#set the canvas
    
    canvas=tk.Canvas(frame_left)
    canvas.grid(row=0,column=0,sticky="news")
    aggfig=FigureCanvasTkAgg(x.fig,canvas)
#    link the scrollbar to the canvas
    scrollcanvas=tk.Scrollbar(frame_left,orient="vertical")
    scrollcanvas.grid(row=0,column=1,sticky='ns')
    canvas.configure(yscrollcommand=scrollcanvas.set)
    
    canvas.config(scrollregion=canvas.bbox("all"))
    aggfig.show()
#   set the first button, show the image
#    ShowPlot=tk.Button(frame_right,text='showimage',height=2,width=9,command=showImg())
#    ShowPlot.pack()
#    set button for adding new points
    ForeMove=tk.Button(frame_right,text='foremove',height=2,width=9,command=hit.hit_foremove)
    ForeMove.pack()
#    set button for backward
    BackMove=tk.Button(frame_right,text='backmove',height=2,width=9,command=hit.hit_backmove)
    BackMove.pack()
#    set button for elongating the pic
    ElongVibra=tk.Button(frame_right,text='elongvibra',height=2,width=9,command=hit.hit_elongate)
    ElongVibra.pack()
#   set button for shortenning the pic
    ShortenVibra=tk.Button(frame_right,text='shortenvibra',height=2,width=9,command=hit.hit_shorten)
    ShortenVibra.pack()
    
    


    
    window.mainloop()    
