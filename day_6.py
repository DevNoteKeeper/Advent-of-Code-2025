

def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        return f.read().splitlines()

def total_sum(numbers):
    return sum(numbers)

def total_multiple(numbers):
    total_multiple = 1
    
    for n in numbers:
        total_multiple *= n
    return total_multiple

def get_problem_column(lines):
    width = max(len(line) for line in lines)
    def is_empty_col(c):
        return all(c >= len(line) or line[c] == ' ' for line in lines)
    
    problems = []
    start = None
    for c in range(width):
        if not is_empty_col(c):
            if start is None:
                start = c
        else:
            if start is not None:
                problems.append((start, c))
                start = None
    if start is not None:
        problems.append((start, width))
    return problems

def parse_numbers_and_signs(lines):
    problems_col = get_problem_column(lines)
    
    numbers = []
    signs = []
    
    for l, r in problems_col:
        nums=[]
        for line in lines[:-1]:
            s=line[l:r].strip()
            if s:
                nums.append(int(s))
                
        numbers.append(tuple(nums))
        
        sign = lines[-1][l:r].strip()
        signs.append(sign)
    return numbers, signs

def parse_numbers_right_to_left(lines, l, r):
    rows = lines[:-1]
    height = len(rows)
    
    cols=[]
    for c in range(l, r):
        col_digits = []
        
        for r_idx in range(height):
            if c<len(rows[r_idx]) and rows[r_idx][c]!=' ':
                col_digits.append(rows[r_idx][c])
                
        if col_digits:
            cols.append(int(''.join(col_digits)))
            
    return list(reversed(cols))

def parse_numbers_and_signs_part2(lines):
    problem_col = get_problem_column(lines)
    
    numbers, signs = [], []
    
    for l, r in problem_col:
        nums = parse_numbers_right_to_left(lines, l, r)
        numbers.append(tuple(nums))
        signs.append(lines[-1][l:r].strip())
    return numbers, signs

# def main():
#     lines = read_file("day_6_input.txt")
    
#     numbers, signs = parse_numbers_and_signs(lines)
#     total = 0
#     for i in range(len(signs)):
#         if(signs[i] == '+'):
#             total += total_sum(numbers[i])
#         if(signs[i] == '*'):
#             total += total_multiple(numbers[i])
            
#     print(total)

def main():
    lines = read_file("day_6_input.txt")
    
    numbers, signs = parse_numbers_and_signs_part2(lines)
    total = 0
    for i in range(len(signs)):
        if(signs[i] == '+'):
            total += total_sum(numbers[i])
        if(signs[i] == '*'):
            total += total_multiple(numbers[i])
            
    print(total)    
    

main()