import re
name=input("Username: ").strip()
name=re.search(r"https?://(www\.)?baidu\.com/(.+)",name)
if name:
    print(f"Username:{name.groups(2)}")