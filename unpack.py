def up(*words):
    up=map(str.upper,*words)
    print(*up)
x=up(["this","is","cs50"])
print(x)