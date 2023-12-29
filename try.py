def main():
    y=get_int()
    print(f"x is {y}")
def get_int():
    while True:
        try:
            x=int(input("what's your name?:"))
        except:
            print("x is not an integer")
        else:
            return x
main()






