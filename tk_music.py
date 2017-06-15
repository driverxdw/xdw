#!/usr/bin/python
#encoding=utf-8
import os
import pygame
from Tkinter import *
import threading
import tkFont
a=list()
n=0
def danqu(entry):
    global a,n
    pygame.mixer.music.load("/home/xdw/music/"+a[n])
    pygame.mixer.music.play()
    entry.insert(END,a[n])
def danquxunhuan():
  for i in a:
    pygame.mixer.music.load("/home/xdw/music/"+i)
    pygame.mixer.music.play(-1,0)
def zanting():
    pygame.mixer.music.pause()
def stop():
    pygame.mixer.music.stop()
def jixu():
    pygame.mixer.music.unpause()
def tuichu():
    exit()   
def xiayiqu(entry):
    global n,a
    if n==len(a)-1:
        print("yuejiela!")
        return
    pygame.mixer.music.stop()
    n+=1
    pygame.mixer.music.load("/home/xdw/music/"+a[n])
    entry.delete('0','end')
    entry.insert(END,a[n])
    pygame.mixer.music.play();
def shangyiqu(entry):
    global n
    if n==0:
        print("yue jie la !")
        return
    pygame.mixer.music.stop()
    n-=1
    pygame.mixer.music.load("/home/xdw/music/"+a[n])
    entry.delete('0','end')
    entry.insert(END,a[n])
    pygame.mixer.music.play() 
def shenyin():
    voice=pygame.mixer.music.get_volume()
    print voice
def main():
    global a
    for j in os.listdir("/home/xdw/music/") :
      if os.path.splitext(j)[1] == '.mp3': 
        a.append(j)
    for ge in a :
       print ge    
    pygame.init()
    root=Tk()
    #设置窗口的大小宽x高+偏移量
    root.geometry('600x300+500+200')
    root.title('MusicBox~')
    entry_font = tkFont.Font(size=10)
    entry = Entry(root, justify="left", font=entry_font)
    entry.grid(row=100, column=100, columnspan=100, sticky=N+W+S+E, padx=50,  pady=30)
    button_font = tkFont.Font(size=100, weight=tkFont.BOLD)
    button_bg = '#D5E0EE'
    button_active_bg = '#E5E35B'
    b1=Button(root,text='bofang',width='5',height='2',command=lambda:danqu(entry)).place(x=50,y=210)
    b2=Button(root,text='zanting',width='5',height='2',command=lambda:zanting()).place(x=450,y=30)
    b3=Button(root,text='tingzhi',width='5',height='2',command=lambda:stop()).place(x=450,y=90)
    b4=Button(root,text='jixubofang',width='5',height='2',command=lambda:jixu()).place(x=450,y=150)
    b5=Button(root,text='tuichu',width='5',height='2',command=lambda:tuichu()).place(x=450,y=210)
    b6=Button(root,text='xiayiqu',width='5',height='2',command=lambda:xiayiqu(entry)).place(x=150,y=210)
    b7=Button(root,text='shangyiqu',width='5',height='2',command=lambda:shangyiqu(entry)).place(x=250,y=210)
    root.mainloop()
if __name__=='__main__':
    main()