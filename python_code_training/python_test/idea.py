import sys
import tkinter as q
import random as t
def main():
    User=input("Are you ready？[y/n]: ").strip()
    User=User.lower()
    if User=='y':
        pan()
    elif User=='n':
        sys.exit("Exit")
    elif User=='Q':
        only_pan()
    else:
        my()
def my():
    User_s=input("Enter? :").strip().lower()
    if User_s=='y':
        p=t.randint(1000,9999)
        print(f"you rootpass {p}")
        User_S=int(input("Input: "))
        if User_S==p:
            only_pan()
        else:
            return False
    else:
        return False

def fun1():
    get=get_number_one()
    get2=get_number_two()
    if get == "Error" or get2 == "Error":
        return "Incorrect input format！"
    if Valid(get,get2):
        result=Result(get,get2)
        result2=Result_2(get,get2)
        result3=Result_3(get,get2)
        return (result,result2,result3)
def fun0():
    print("Input you number(hint:[0-9])")
    x=int(input(": "))
    print("Note that Enter with commmas(,)")
    R=[]
    r=0
    flag=False
    try:
        y=input("Input matrix: ").split(",")
        if len(y)==9:
            n=len(y)/3
            flag=True
        if len(y)==4:
            n=len(y)/2
            flag=True
        for i in range(len(y)):
            if (i==n or i/3==2) and flag==True:
                print('\n')
            print(int(y[i])*x,end=' ')
    except:
        print("Invalid input")
        return False
    return True
def fun2_Valid(a,b):
    if len(a)!=len(b):
        return False
    return True
    
    
def fun2():
    print("Note that Enter with commmas(,)")
    print("One matrix,one row of input!")
    x=input("The first Matrix input: ").split(",")
    y=input("The second Matrix input: ").split(",")
    z=[]
    if fun2_Valid(x,y):
        for i in range(len(x)):
            z.append(int(x[i])+int(y[i]))
        return z
    else:
        print("Invalid Matrix")
        print("Please input again")
        return False
    
def fun3():
    print("Note that Enter with commmas(,)")
    x=input("The first Matrix input: ").split(",")
    y=input("The second Matrix input: ").split(",")
    z=[]
    if fun2_Valid(x,y):
        for i in range(len(x)):
            z.append(int(x[i])-int(y[i]))
        return z
    else:
        print("Invalid Matrix")
        print("Please input again")
        return False
def fun4():
    print("❤️")
    return 1
def fun5():    
    print("❤️")
    return 1
def fun6():
    ...
def pan():
    print("|---------------------------------------|")
    print("|-+++++Matrix Operations(Standard)+++++-|")
    print("|----Input 1:Matrix Manipulation--------|")
    print("|----Input 2:Matrix by Matrix-----------|")
    print("|----Input 3:Exit system----------------|")
    print("|---------------------------------------|")
    print("|-----Note:Only 3 by 3 Matrix-----------|")
    print("|---------------------------------------|")
    while True:
        u=input("Input : ").strip()
        if u=='1':
            if fun0():
                print("\nFinish")
        elif u=='2':
            Re_f1=fun1()
            for i in Re_f1:
                print(i)
        elif u=='3':
            sys.exit("Exit")
        else:
            print("The input is invalid")
def only_pan():
    print("|---------------------------------------|")
    print("|-+++++Matrix Operations(Advanced)+++++-|")
    print("|----Input 1:Matrix Manipulation--------|")
    print("|----Input 2:Matrix by Matrix-----------|")
    print("|----Input 3:Matrix plus Matrix---------|")
    print("|----Input 4:Matrix subtract Matrix-----|")
    print("|----Input 5:Exit system----------------|")
    print("|----Input 6:Surprise-------------------|")
    print("|---------------------------------------|")
    print("|----Note:Only 3 by 3 Matrix------------|")
    print("|---------------------------------------|")
    while True:
        u=input("Input: ").strip()
        if u=='1':
            Re_f0=fun0()
            print(Re_f0)
        elif u=='2':
            Re_f1=fun1()
            for i in Re_f1:
                print(i)
        elif u=='3':
            Re_f2=fun2()
            for j in range(len(Re_f2)):
                print(Re_f2[j],end=' ')
                if j==2 or j==5:
                    print("\n")
            print('\n')
                    
        elif u=='4':
            Re_f3=fun3()
            for j in range(len(Re_f3)):
                print(Re_f3[j],end=' ')
                if j==2 or j==5:
                    print("\n")
            print('\n')
        elif u=='5':
            sys.exit("Exit")
        elif u=='6':
            fun4()
        elif u=='show':
            fun5()
        else:
            print("Invalid")


def get_number_one():
    print("*The First Matrix")
    print("Note that Enter with commmas(,)")
    try:
        x=input("Input the first line: ").split(",")
        y=input("Input the second line: ").split(",")
        z=input("Input the third line: ").split(",")
        return (x,y,z)
    except:
        return "Error"

def get_number_two():
    print("*The Second Matrix")
    print("Note that Enter with commmas(,)")
    try:
        x=input("Input the first line: ").split(",")
        y=input("Input the second line: ").split(",")
        z=input("Input the third line: ").split(",")
        return (x,y,z)
    except:
        return "Error"

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



def For(m,time,space):
    Time=time #元素索引
    row=space #行数
    for i in range(len(m[row])):
        return m[row][Time]

def Valid(x,y):
    w,h=1,1
    w2,h2=1,1
    for i in x:
        w+=1
        for j in i:
            h+=1
    for n in y:
        w2+=1
        for m in n:
            h2+=1
    if (w == w2 and h == h2) or (w == h2 and h == w2):
        return True
    else:
        print("The input is invalid")
        return False



if __name__=="__main__":
    main()
