import csv

x=input("what's you name:")
y=int(input("what's you age:"))
with open('man.csv','a') as file:
    w=csv.DictWriter(file,fieldname='x','y')
    w.writerow({'y':y,'x':x})


