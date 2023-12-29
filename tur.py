class flag:
    def __init__(self,first,last):
        if first=='':
            raise ValueError("first is None")
        self.first=first
        self.last=last
    def __str__(self):
        return f"{self.first},{self.last}"
    @property
    def last(self):
        return self._last
    @last.setter
    def last(self,last):
        if last == 'matt':
            raise ValueError("last is invalid")
        self._last=last
def main():
    name=get_name()
    name._last='matt'
    print(name)
def get_name():
    first=input("first name>>")
    last=input("last name>>")
    return flag(first,last)

if __name__=='__main__':
    main()