def main():
    x=number()
    cat(x)
def number():
    while True:
        y=int(input("what's you number:"))
        if y>0:
            return y
def cat(n):
    for i in range(n):
        print("hello!")
main()