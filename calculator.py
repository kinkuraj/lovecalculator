firstname = input("Enter first person name:")
secondname = input("Enter second person name:")

name = firstname + secondname
name = name.replace(" ","")
#print(name)
list = []
for x in name:
    count = name.count(x)
    if count > 0:
        list.append(count)
        name = name.replace(x,"").strip()

#print(list)

def addnums(list):
    newlist = []
    while len(list) > 1:
        newlist.append(list.pop()+list.pop(0))
    else:
        newlist.extend(list)
    
    if len(newlist) > 2 :
        #print(newlist)
        addnums(newlist)
    elif len(newlist) > 1:
        lastnum = int(str(newlist[0])+str(newlist[1]))
        #print(lastnum)
        if lastnum > 100:
            print ("100 %")
        else: 
            print(str(newlist[0])+str(newlist[1])+"%")
    else:
        print(str(newlist[0]) + "%")

addnums(list)
