from collections import deque

def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        return f.read().splitlines()
    
def count_beam_splits(grid):
    h = len(grid)
    w = len(grid[0])
    
    for r in range(h):
        for c in range(w):
            if grid[r][c] =='S':
                start_row, start_col = r, c
                break
    
    queue = deque()
    queue.append((start_row+1, start_col))
    
    visited_splitters = set()
    split_count = 0
    
    while queue:
        r, c = queue.popleft()
        
        if r >= h or c < 0 or c>=w:
            continue
        cell = grid[r][c]
        
        if cell == '.':
            queue.append((r+1, c))
        elif cell == '^':
            if(r, c) not in visited_splitters:
                visited_splitters.add((r, c))
                split_count += 1
                
                queue.append((r+1, c-1))
                queue.append((r+1, c+1))
                
    return split_count

def count_beam_splits_part2(grid):
    h = len(grid)
    w = len(grid[0])
    
    for r in range(h):
        for c in range(w):
            if grid[r][c] =='S':
                start_row, start_col = r, c
                break
    
    memo = {}
    
    def dfs(r,c):
        if r>= h or c<0 or c>=w:
            return 1
        if (r, c) in memo:
            return memo[(r, c)]
        cell = grid[r][c]
        
        if cell == '.':
            count = dfs(r+1,c)
        elif cell == '^':
            count = dfs(r+1, c-1) + dfs(r+1, c+1)
        else:
            count = 0    
        memo[(r, c)] = count    
        return count
    
    return dfs(start_row + 1, start_col)        
        
   

def main():
    line = read_file('day_7_input.txt')
    total_split = count_beam_splits_part2(line)
    print(total_split)
    
main()