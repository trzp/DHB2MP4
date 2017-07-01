#coding:utf-8   
from Tkinter import *
import os
from tkFileDialog import askdirectory

'''
author:mrtang
date:2017.7
version:1.0
email:mrtang@nudt.edu.cn

This script is used to transfer .BHD files to .mp4 files.
'''

def getpath():
    path = askdirectory()
    pathstr.set(path)
    cue.set('ready!')

def start():
    path = e1.get()
    files = os.listdir(path)
    for file in files:
        k = file.split('.')
        newname = k[0]+'.mp4'
        os.rename(os.path.join(path,file),os.path.join(path,newname))
    cue.set('completed!')
    

root = Tk()
pathstr = StringVar()
cue = StringVar()
cue.set('ready!')
Label(root,text=u'该程序将暴风影音文件转码为mp4文件').grid(row=0, column=0)
e1 = Entry(root,textvariable=pathstr,width=40)
e1.grid(row=1,column=0)
Button(root, text=u"选择路径",command=getpath).grid(row=1,column=1)
Entry(root,textvariable=cue,width=40).grid(row=2,column=0)
Button(root, text=u"开始转码",command=start).grid(row=2,column=1)
mainloop()
