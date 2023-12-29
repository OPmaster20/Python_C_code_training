import tkinter as t
from tkinter import ttk
from PIL import *
import time
import sys
window=t.Tk()
window.title("📚矩阵运算器")
window.geometry('377x600')
window.configure(background='pink')
#canvas=t.Canvas(window,width=800,height=550,bd=0)
#imgpath='hu.gif'
#window.configure(backgroud='pexels-pixabay-289225.jpg')
#img=Image.open(imgpath)
#photo=ImageTK.PhotoImage(img)
#canvas.create_image(700,500,image=photo)
#canvas.pack()
#canvas.create_window(100,50,width=100,height=20,)
text_input_main=t.Text(window,width=41,height=11)
text_input_main.place(x=30,y=30)
text_input_main.insert('insert','|----Matrix Analysis(Version 0.1)-------|\n')
text_input_main.insert('insert','|---------------------------------------|\n')
text_input_main.insert('insert','|----Input matrix:Matrix Manipulatio----|\n')
text_input_main.insert('insert','|----Input 2matrix:Matrix by Matrix-----|\n')
text_input_main.insert('insert','|----Input exit:Exit system-------------|\n')
text_input_main.insert('insert','|----Input sup:Surprise-----------------|\n')
text_input_main.insert('insert','|---------------------------------------|\n')
text_input_main.insert('insert','|---------------------------------------|\n')
text_input_main.insert('insert','|---------------------------------------|\n')
text_input_main.insert('insert','|----Note:Only 3 by 3 Matrix------------|\n')
text_input_main.insert('insert','|---------------------------------------|\n')
button=t.Button(window,text='Exit',command=lambda:window.destroy(),width=4,height=1)
button.place(relx=0,rely=1,anchor='sw')



def By():
    frame=t.Frame(width=290,height=180,bg='#FFFAF0')
    frame.place(x=32,y=220)
    text=t.Text(frame,width=35,height=1)
    text.place(x=25,y=20)
    text.insert("insert","Select you number and input Matrix\n")
    
    text=t.Text(frame,width=35,height=1)
    text.place(x=25,y=150)
    text.insert("insert","Enter quit to exit the panel\n")
    
    select=ttk.Combobox(frame,width=2,textvariable=t.IntVar(),state='readonly')
    lis=[0,1,2,3,4,5,6,7,8,9]
    select['values']=lis
    select.place(x=31,y=50)
    entry=t.Entry(frame,width=14)
    entry.place(x=31,y=90)
    button=t.Button(frame,text='N/C',command=lambda:Select(select),width=1,height=1)
    button.place(x=200,y=50)
    button2=t.Button(frame,text='M/C',command=lambda:Select(entry),width=1,height=1)
    button2.place(x=200,y=90)
    window.mainloop()
def Matrix():
    frame=t.Frame(width=290,height=180,bg='#F8F8FF')
    frame.place(x=32,y=390)
    text=t.Text(frame,width=35,height=1)
    text.place(x=25,y=20)
    text.insert("insert","Note that Enter with commmas(,)\n")
    
    text_input=t.Text(frame,width=9,height=3)
    text_input.place(x=25,y=60)
    text_input2=t.Text(frame,width=9,height=3)
    text_input2.place(x=105,y=60)

    select=ttk.Combobox(frame,width=2,textvariable=t.IntVar(),state='readonly')
    lis=['+','-','*']
    select['values']=lis
    select.place(x=25,y=120)
    '''
    text_input_main.insert('insert','|---------------------------------------|\n')
    
    text_input_main.insert('insert',"| For example: [0-9] Click N/C          |\n")
    text_input_main.insert('insert',"|   [1,2,3,4,5,6,7,8,9] Click M/C       |\n")
    text_input_main.insert('insert',"|                                       |\n")
    text_input_main.insert('insert',"| Note: Make sure you input format is   |\n")
    text_input_main.insert('insert',"|         correct                       |\n")
    text_input_main.insert('insert',"|                                       |\n")
    text_input_main.insert('insert',"|                                       |\n")
    text_input_main.insert('insert',"|                                       |\n")
    text_input_main.insert('insert',"|*************-----BFQM-----************|\n")
    text_input_main.insert('insert','|---------------------------------------|\n')
    '''

    button2=t.Button(frame,text='M/M/M',command=lambda:Matrix_by(text_input,text_input2,select),width=3,height=1)
    button2.place(x=180,y=70)
    #button3=t.Button(frame,text='Clear',command=lambda:Clear(text_input,text_input2,select),width=3,height=1)
    #button3.place(x=200,y=70)
def Exit():
    ...

def Clear(x,y,z):
    if x and y and z:
        #text_input.delete(1.0,"end")
        #text_input2.delete(1.0,"end")
        return 'ok'
    
def Valid(x,y):
    if x!=y:
        return False
    return True

def Result(n,m):
    v=[]
    Time=0
    Space=0
    k=0
    i=0
    j=0
    ci=1
    while True:
        s=For(m,Time,Space)
        k+=int(n[i][j])*int(s)
        j+=1
        Space+=1
        if Space>2:
            v.append(k)
            ci+=1
            j=0
            i=0
            Time+=1
            Space=0
            k=0
        if ci>3:
            break
            
        if i==2 and Time==2:
            break
    return v
def Result_2(n,m):
    v=[]
    Time=0
    Space=0
    k=0
    i=1
    j=0
    ci=1
    while True:
        s=For(m,Time,Space)
        k+=int(n[i][j])*int(s)
        j+=1
        Space+=1
        if Space>2:
            v.append(k)
            ci+=1
            j=0
            i=1
            Time+=1
            Space=0
            k=0
        if ci>3:
            break
            
        if i==2 and Time==2:
            break
    return v

def Result_3(n,m):
    v=[]
    Time=0
    Space=0
    k=0
    i=2
    j=0
    ci=1
    while True:
        s=For(m,Time,Space)
        k+=int(n[i][j])*int(s)
        j+=1
        Space+=1
        if Space>2:
            v.append(k)
            ci+=1
            j=0
            i=2
            Time+=1
            Space=0
            k=0
        if ci>3:
            break
    return v

def Fun(get,get2):
    result=Result(get,get2)
    result2=Result_2(get,get2)
    result3=Result_3(get,get2)
    return (result,result2,result3)
    
def For(m,time,space):
    Time=time #元素索引
    row=space #行数
    for i in range(len(m[row])):
        return m[row][Time]

def Shellfe(k):
    a=[]
    b=[]
    c=[]
    gross=[]
    for j in range(len(k)):
        if len(a)!=3:
            a.append(k[j])
        elif len(b)!=3 and j>2:
            b.append(k[j])
        elif len(c)!=3 and j>5:
            c.append(k[j])
    gross=[a,b,c]
    return gross

def Fun2(x,y,n):
    z=[]
    if str(n)=='-':
        for i in range(len(x)):
            z.append(int(x[i])-int(y[i]))
    else:
        for j in range(len(x)):
            z.append(int(x[j])+int(y[j]))
    return z
            
            

def Matrix_by(x,y,z):
    text_x=[]
    text_y=[]
    X=(x.get(0.0,'end').replace(" ","")).split('\n')
    X.pop()
    for i in X:
        d=i.split(',')
        for j in d:
            text_x.append(j)
            
    Y=(y.get(0.0,'end').replace(" ","")).split('\n')
    Y.pop()
    for h in Y:
        o=h.split(',')
        for a in o:
            text_y.append(a)
    print(text_x)
    print(text_y)
            
    b=0
    if Valid(len(text_x),len(text_y)) and str(z.get())=='*':
        n=Shellfe(text_x)
        m=Shellfe(text_y)
        Re=Fun(n,m)
        text_input_main.delete(1.0,"end")
        for n in range(len(Re)):
            text_input_main.insert('insert',str(Re[n])+'\n')
        text_x.clear()
        text_y.clear()
    else:
        print('Valid')
    if Valid(len(text_x),len(text_y)) and str(z.get())!='*':
        Rt=Fun2(text_x,text_y,z.get())
        print(Rt)
        text_input_main.delete(1.0,"end")
        if len(Rt)==9:
            b=len(Rt)/3
        if len(Rt)==4:
            b=len(Rt)/2
        for i in range(len(Rt)):
            if i==b or i/3==2:
                text_input_main.insert('insert','\n')
            text_input_main.insert('insert',str(Rt[i]))
            text_input_main.insert('insert',' ')
        text_x.clear()
        text_y.clear()
    else:
        print('Valid')

Number=0
def Select(self):
    re=[]
    R=[]
    r=0
    v=[]
    n=0
    flag=False
    
    try:
        if len(self.get())==1:
            global Number
            Number=self.get()
        if len(self.get())>2:
            if str(self.get())=='quit':
                return 'quit'
            k=self.get().split(',')
            for i in k:
                v.append(int(i))
            print(v)
            if len(v)==9:
                n=len(v)/3
                flag=True
            if len(v)==4:
                n=len(v)/2
                flag=True
            text_input_main.delete(1.0,"end")
            for i in range(len(v)):
                if (i==n or i/3==2) and flag==True:
                    text_input_main.insert('insert','\n')
                text_input_main.insert('insert',int(v[i])*int(Number))
                text_input_main.insert('insert',' ')
            return 'pass'
    except:
        text_input_main.delete(1.0,"end")
        text_input_main.insert('insert','Input-error\n')
    

def main(self):
    if str(self.get())=='matrix':
        text_input_main.delete(1.0,"end")
        By()
    elif str(self.get())=='2matrix':
        text_input_main.delete(1.0,"end")
        Matrix()
    elif str(self.get())=='exit':
        window.destroy()
    else:
        text_input_main.delete(1.0,"end")
        text_input_main.insert('insert',"I don't know what that means\n")
        
        
    

entry=t.Entry(window,width=20)
entry.place(x=30,y=190)
button=t.Button(window,text='Choose',command=lambda:main(entry),width=6,height=1)
button.place(x=230,y=189)
window.mainloop()
    
