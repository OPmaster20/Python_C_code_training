List=[ "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
while True:
    try:
        x,y,z=input("Date:").split('/')
        if int(y)>31 or int(z)<1500 or int(x)>12 or int(x)==0:
            continue
        if int(x)<10 or int(y)<10:
            print(f"{z}-0{x}-0{y}")
        else:
            print(f"{z}-{x:02}-{y:02}")
            break
    except:
        x2,y2,z2=input("Date:").split(' ')
        for i in range(len(List)):
            if x2==List[i] and int(y2)<10:
                print(f"{z2}-{i}-0{y2}")
                break
            elif x2==List[i] and 10<=int(y2)<31:
                break
            else:
                continue
        pass


