items = [6,10,13,17,25,39,48,50,67]

def binarySearch(item, itemlist):
    lowerIdx = 0
    upperIdx = len(itemlist)-1
    
    while lowerIdx <= upperIdx:
        midIdx = (lowerIdx+upperIdx)//2
        
        if itemlist[midIdx] == item:
            return midIdx
        
        if item > itemlist[midIdx]:
            lowerIdx = midIdx+1
        else:
            upperIdx = midIdx-1
    
    if lowerIdx > upperIdx:
        return None
    

print(binarySearch(10, items))
print(binarySearch(67, items))
print(binarySearch(100, items))
        