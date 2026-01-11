import heapq
from itertools import combinations

# ---------------- Union-Find 클래스 ----------------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n  # 각 component 크기

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]
        return True

# ---------------- 파일 읽기 ----------------
def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        lines = f.read().splitlines()
        points = [tuple(map(int, line.strip().split(','))) for line in lines]
    return points

# ---------------- 거리 계산 ----------------
def distance_squared(p1, p2):
    # 변경: sqrt 제거 → 비교만 필요, 속도/정확도 향상
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

# ---------------- Edge 생성 ----------------
def generate_edges(points):
    for i, j in combinations(range(len(points)), 2):
        yield (distance_squared(points[i], points[j]), i, j)

# ---------------- 연결 함수 ----------------
def connect_closest(points, num_connections=1000):
    n = len(points)
    uf = UnionFind(n)

    # 변경: generator를 바로 heap에 push → 메모리 최적화
    min_heap = []
    for edge in generate_edges(points):
        heapq.heappush(min_heap, edge)

    # 가능한 최대 연결보다 num_connections 크면 제한
    max_possible_connections = n*(n-1)//2
    num_connections = min(num_connections, max_possible_connections)

    # 변경: 문제 요구사항에 맞게 union 성공 여부와 관계없이 가장 가까운 num_connections 쌍 사용
    connections_done = 0
    while min_heap and connections_done < num_connections:
        d, i, j = heapq.heappop(min_heap)
        uf.union(i, j)  # 성공 여부와 관계없이 count
        connections_done += 1

    # component 크기 계산
    sizes = {}
    for idx in range(n):
        root = uf.find(idx)
        sizes[root] = uf.size[root]

    # 상위 3개 component 곱 계산, 부족하면 1로 채움
    top3 = sorted(sizes.values(), reverse=True)[:3]
    while len(top3) < 3:
        top3.append(1)  # 부족하면 1로 채움

    return top3[0] * top3[1] * top3[2]

# ---------------- main ----------------
def main():
    points = read_file('day_8_input.txt')
    result = connect_closest(points, num_connections=1000)
    print(result)

if __name__ == "__main__":
    main()
