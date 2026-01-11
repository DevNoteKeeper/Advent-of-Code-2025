def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        text = f.read()
    values = text.split(",")
    return values
 
def checkIDs(values):
    ids = set()
    
    for v in values:
        parts = v.split("-")
        ids.add(tuple(parts))
    return ids

def isLenEven(value):
    value = str(value)
    return len(value) %2 == 0        

def checkId(left, right):
    id_count = 0
    left = int(left)
    right = int(right)
    
    for i in range(left, right+1):
        s = str(i)
        if(isLenEven(s)):
            halfPoint = len(s)//2
            
            if(s[:halfPoint] == s[halfPoint:]):
                id_count += i
                
    return id_count    

def isInvaild(left, right):
    id_count = 0
    left = int(left)
    right = int(right)
    
    for i in range(left, right+1):
        s = str(i)
        l = len(s)
        
        for k in range(1, l):
            if l%k != 0:
                continue
            repeat = l//k
            if repeat <2:
                continue
            pattern = s[:k]
            if (pattern * repeat == s):
                id_count += i
                break
    return id_count  
def main():
    values = read_file("day_2_input.txt")
    ids = checkIDs(values)
    
    totalIdCount = 0
    for left, right in ids:
        totalIdCount += isInvaild(left, right)
    
    print(totalIdCount)
    
main()