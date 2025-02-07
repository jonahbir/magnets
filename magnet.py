def magnets():
    store=[]
    group=1
    number=int(input())
    x=input()
    store.append(x)
    for i in range(number-1):
        new_magnet=input()
        popped_magnet=store[-1]
        store.pop(-1)
        if new_magnet==popped_magnet:
            store.append(new_magnet)
        else:
            group+=1
            store.append(new_magnet)
    return group 
print(magnets())



        

