from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import fileinput

def serchORmakerul():
    p1=args1.get()
    p2=valargs1.get()
    p3=args2.get()
    p4=valargs2.get()

    if sleds.get()!='':
        for line in fileinput.input('rules.txt',inplace=True):
            if '{}'.format(p1.strip()+''+p2.strip()+''+p3.strip()+''+p4.strip()+'') in line:
                continue
            print(line.rstrip('\n'))

        frul=open('rules.txt','a')
        frul.write(p1.strip()+''+p2.strip()+''+p3.strip()+''+p4.strip()+''+sleds.get()+'\n')
        frul.close()
    else
        templist=[p1.strip(),p2.strip(),p3.strip(),p4.strip()]
        frul=open('rules.txt','r')
        for lines in frul:
            rullist=lines.split(maxsplit=4)
            if rullist[:4]=templist:
                sleds.insert(0,rullist[4])
        if sleds.get()=='':
            err=messagebox.showerror('Ошибка','Правило отсутствует!')

def savearg():

print('hello')




print('This is a new code here")
