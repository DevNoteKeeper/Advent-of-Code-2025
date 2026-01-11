def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        return f.read()
    

def part_1(start, lines):
    pos = start
    for line in lines:
        x = int(line[1:])
        if(line[0] == 'L'):
            pos = (pos-x)%100
            
        if(line[0] == 'R'):
            pos = (pos+x)%100

        if(pos == 0):
            count = count+1
            
def part_2(start, lines):
    pos = start
    count = 0
    for line in lines:
        x = int(line[1:])
        if(line[0] == 'L'):
            c, pos =  check_pass_zero_negative(pos, x)
            count = c+count
            
        if(line[0] == 'R'):
            c, pos =  check_pass_zero_positive(pos, x)
            count = c+count
            
    return count
            
    
def check_pass_zero_negative(pos, x):
    count = 0
    for _ in range(x):
        pos = (pos-1)%100
        if pos == 0:
            count +=1
            
    return count, pos

def check_pass_zero_positive(pos, x):
    count = 0
    for _ in range(x):
        pos = (pos+1)%100
        if pos == 0:
            count +=1
            
    return count, pos

def main():
    start = 50
    
    inputFile = read_file('day_1_input.txt')
    lines = inputFile.strip().splitlines()
    
    count = 0
    # part_1(start, lines)
    
    count = part_2(start, lines)
    
    print('count = ', count)
    
main()

