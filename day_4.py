def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        text = f.read().splitlines()
        return text

    
def check_at(lines):
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                if check_around(i, j, lines) == True:
                    total +=1   
    return total

    
def check_around(i, j, lines): 
    count = 0   
    for a in range(i-1, i+2):
        for b in range(j-1, j+2):
            if a<0 or b<0:
                continue
            if a>=len(lines) or b>=len(lines[i]):
                continue
            if a==i and b==j:
                continue
            if lines[a][b] == '@':
                count += 1

    if count < 4:
        return True
    else: return False
                
def find_accessible(lines):
    positions=[]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '@' and check_around(i, j, lines):
                positions.append((i, j))
    return positions              
        
# def main():
#     total_count = 0
#     lines = read_file("day_4_input.txt")
#     total_count += check_at(lines)
    
#     print(total_count)

def main():
    lines = read_file("day_4_input.txt")
    total_removed = 0
    
    while True:
        accessible = find_accessible(lines)
        if not accessible:
            break
        for i, j in accessible:
            lines[i] = lines[i][:j] + '.'+lines[i][j+1:]
        total_removed += len(accessible)
        
    print(total_removed)
    
main()