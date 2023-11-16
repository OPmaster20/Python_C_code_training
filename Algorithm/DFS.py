vertex_set1 = [1,4,5,8]
vertex_set2 = [2,6]
vertex_set3 = [7,3]
vertex_stack = []

index = 0;
# branch of set1 : (head)1 -> 4 -> 5 -> 8(end)
# branch of set2 : (head)1 -> 2 -> 6(end)
# branch of set3 : (head)6 or (head)2 -> 7 -> 3(end)

def DFSS(vertex = []):
    global index
    length = len(vertex)
    if len(vertex_stack) == 0:
        for i in range(length):
            index = index + 1
            vertex_stack.append(vertex[i])
            print(vertex_stack[i])
        vertex_stack.remove(vertex_stack[length - 1])
        index = index - 1
    else:
        for j in range(length):
            vertex_stack.insert(index,vertex[j])
            print(vertex_stack[index])
            index = index + 1
        index = index - 1
        vertex_stack.remove(vertex_stack[index])


def Init():
    DFSS(vertex_set1)
    DFSS(vertex_set2)
    DFSS(vertex_set3)

    print(vertex_stack)
    

if __name__ == "__main__":
    Init()