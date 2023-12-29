
class Nick:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x} and {self.y}"
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Nick(x,y)
C=Nick(4,6)
print(C)
D=Nick(34,12)
print(D)

B=C+D
print(B)

