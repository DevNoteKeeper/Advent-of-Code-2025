def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        return f.read().splitlines()

def parse_input(lines):
    ranges=[]
    # ids=[]
    
    for i in lines:
        if i == "":
            continue
        if "-" in i:
            start, end = i.split('-')
            ranges.append((int(start), int(end)))
    #     else:
    #         ids.append(int(i))
            
    # return ranges, ids
    return ranges

# def is_fresh(i, ranges):
#     for start, end in ranges:
#         if start<= i <= end:
#             return True
#     return False

# def check_fresh_num(ranges):
#     numbers = set()
    
#     for start, end in ranges:
#         numbers.update(range(start, end+1))
            
#     return numbers

def count_fresh_ids(ranges):
    # 1. 시작점 기준 정렬
    ranges.sort()
    
    total = 0
    current_start, current_end = ranges[0]
    
    for start, end in ranges[1:]:
        if start > current_end:
            # 새로운 범위가 겹치지 않을 때
            total += current_end - current_start + 1
            current_start, current_end = start, end
        else:
            # 겹치면 끝점 갱신
            current_end = max(current_end, end)
    
    # 마지막 범위 포함
    total += current_end - current_start + 1
    return total
              
# def main():
#     total_fresh = 0
#     lines = read_file("day_5_input.txt")
#     ranges, ids = parse_input(lines)
    
#     for i in ids:
#         if is_fresh(i, ranges):
#             total_fresh +=1
            
#     print(total_fresh)


def main():
    lines = read_file("day_5_input.txt")
    ranges = parse_input(lines)
    
    numbers = check_fresh_num(ranges)
    print(len(numbers))
    
main()