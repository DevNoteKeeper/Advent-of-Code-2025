def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        text = f.read().splitlines()
    return text

def find_two_digit(line: str) -> int:
    digits = [int(c) for c in line]
    best = 0
    n = len(digits)
    
    for i in range(n):
        for j in range(i+1, n):
            best = max(best, digits[i]*10+digits[j])
            
    return best

def larger_joltage(line: str) -> int:
    digits = [int(c) for c in line]
    n = len(digits)
    remove = n-12
    
    stack =[]
    
    for i in line:
        while remove > 0 and stack and stack[-1] < i:
            stack.pop()
            remove-=1
        stack.append(i)
        
    if remove > 0:
        stack = stack[:-remove]
        
    result = ''.join(stack[:12])
    return int(result)

def main():
    lines = read_file("day_3_input.txt")
    # total = sum(find_two_digit(line.strip()) for line in lines if line.strip())

    total = 0
    for line in lines:
        line = line.strip()
        # if line:
        #     total += find_two_digit(line)
        
        if line:
            total += larger_joltage(line)
    print(total)

    
main()