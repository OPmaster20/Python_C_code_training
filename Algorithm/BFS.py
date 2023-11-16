q = []
l = 0

def BFS(a,n):
    global l
    i = 0
    j = 0
    while(i < len(a)):
        while(j < len(a[0])):
            if n == a[i][j]:
                
            else:
                if a[i][j] != 0:
                    q.append(a[i][j])
            j += 1
        i += 1




def init():
    a = [[0,5,0],[6,0,4],[0,1,0],[7,0,2],[0,3,0]]
    n = int(input("Search number: "))
    BFS(a,n)

if __name__ == "__main__":
    init()