import re
x=input("what's you email?").strip()
if re.search(r'^\w+@(\w|\w+\.)+\.edu$',x):
    print('valid')
else:
    print('invalid')
