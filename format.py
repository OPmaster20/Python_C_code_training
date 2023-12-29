import re
name=input("what's you name").strip()
math=re.search(f"^(.+), (.+)$",name)
if math:
    last,first=math.groups()
    name=f'{first} {last}'
    print(name)
