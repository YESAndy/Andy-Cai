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

data=pd.read_csv(r'C:\Users\ANDY\Desktop\L0207.csv')
time=[]

for i in data['Time(ms)']:
    time.append(i)
del data['Time(ms)']

offset=0
times=np.arange(1,2049)  
step=1        
hit_fore=True
hit_back=True
hit_show=False
hit_elong=True
hit_short=True
hit_switch=True

class VibraGraph:
    
 

#    step,number=2048,number*step+1    
    def add_xvibra(self,xvibra):
        return xvibra
    
    def minor_xvibra(self):
        pass
    
    def switchStep(self,step):
        time=np.arange(1,step*2048+1,step)
        return time
        
    def plotvibra(self,xvibra,time,ax):
        ax.plot(xvibra,time,'k')
        
    def fillblank(self,xvibra,time,offset,ax):
        ax.fill_betweenx(time,offset,xvibra,where=(xvibra>offset),color='k')
        
    def set_xvibralim(self,left,right,ax):
        ax.set_xlim(left,right)
    

        
    
    
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
            x.minor_xvibra
        else:
             hit_back=True

    def hit_elongate(self):
        global hit_elong,hit_show
        if hit_elong == True:
            hit_show=True
            hit_elong=False
        else:
             hit_elong=True

    def hit_shorten(self):
        global hit_short,step
        x=VibraGraph()
        if hit_short == True:
            if step>0:
                step=step-1
                x.switchStep(step)
            else:
                pass
        else:
             hit_short=True

    def hit_showimg(self):
        global hit_show,step,times
        x=VibraGraph()
        if hit_show == True:
            step=step+200
            times=x.switchStep(step)
            return x.showImg(data,0,times)
            hit_show=False
             

    def hit_switchimg(self):
        global hit_switch
        if hit_switch == True:
            hit_switch=False
        else:
             hit_switch=True
        
     
if __name__=='__main__':
    
    hit=hit_condition()
    fig,ax=plt.subplots()
    x=VibraGraph()

    for i in range(1,81):
        testdata1=pd.to_numeric(data[str(i)])+offset
        x.plotvibra(testdata1,times,ax)
        x.fillblank(testdata1,times,offset,ax)
        offset=offset+3000



#    initialize window
    window=tk.Tk()
    window.title('vibrationgraphtest')

    
#   set the first button, show the image
    ShowPlot=tk.Button(window,text='showimage',height=2,width=8,command=hit.hit_showimg)
    ShowPlot.pack()
#    set button for adding new points
    ForeMove=tk.Button(window,text='foremove',height=2,width=8,command=hit.hit_foremove)
    ForeMove.pack()
#    set button for backward
    BackMove=tk.Button(window,text='backmove',height=2,width=8,command=hit.hit_backmove)
    BackMove.pack()
#    set button for elongating the pic
    ElongVibra=tk.Button(window,text='elongvibra',height=2,width=8,command=hit.hit_elongate)
    ElongVibra.pack()
#   set button for shortenning the pic
    ShortenVibra=tk.Button(window,text='shortenvibra',height=2,width=8,command=hit.hit_shorten)
    ShortenVibra.pack()
    
#set the canvas
    canvas=FigureCanvasTkAgg(fig,master=window)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)
    
    window.mainloop()    
