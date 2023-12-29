def main():
    width,height=str(input("what's you heght and width?")).split(",")
    print_pop(int(width),int(height))
def print_pop(w,h):
    for i in range(h):
        for j in range(w):
            print("#",end='')
        print('\n')

main()