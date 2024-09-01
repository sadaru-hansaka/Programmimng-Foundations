items = [12,3,154,65,9,50,82,190,200]

def search (item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i
    return None
        

ans1 = search(100,items)
ans2 = search(3,items)
print(ans1)
print(ans2)