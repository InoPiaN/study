# 🚀 Algorithm Study

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Study-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

---

## 📌 Overview
코딩 테스트 대비를 위해 알고리즘 문제를 풀이하며  
👉 **핵심 개념 / 패턴 / 문제 해결 흐름**을 정리한 레포입니다.

---

## 🧠 Problem Solving Flow

```text
1. 완전탐색 가능 여부 판단
2. 최적화 필요 시 알고리즘 선택
3. 상태 정의
4. 구현
5. 시간복잡도 검증
```

### 빠른 체크 포인트
- **완전탐색**: N이 작고, 가능한 경우의 수가 제한적인가?
- **정렬**: 정렬하면 관계가 단순해지는가?
- **해시**: 빠른 조회나 카운팅이 필요한가?
- **DP**: 같은 상태가 반복되는가?
- **그래프**: 연결 관계 / 선후 관계 / 최단거리가 핵심인가?

---

# ⚙️ Algorithms

---

## 📌 Prefix Sum (부분합)

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
배열의 구간합을 빠르게 계산하기 위한 기법

### 핵심 아이디어
- 미리 누적합을 계산해두면 구간합을 O(1)에 구할 수 있다.
- `prefix[i]`를 **0번부터 i-1번까지의 합**으로 정의하면 관리가 편하다.

### 기본 예시
```python
arr = [1, 2, 3, 4]

prefix = [0] * (len(arr) + 1)
for i in range(1, len(arr) + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

# arr[1] ~ arr[2] = 2 + 3
left = 1
right = 3   # prefix는 right를 열린 구간처럼 생각
print(prefix[right] - prefix[left])   # 5
```

### 2차원 부분합 예시
```python
board = [
    [1, 2],
    [3, 4]
]

n = len(board)
m = len(board[0])

prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = (
            prefix[i - 1][j]
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]
            + board[i - 1][j - 1]
        )

# (0,0) ~ (1,1) 전체 합
print(prefix[2][2] - prefix[0][2] - prefix[2][0] + prefix[0][0])   # 10
```

### 언제 쓰나?
- 구간합
- 연속 부분 수열 합
- 2차원 배열의 직사각형 합

### 핵심 포인트 🔥
- `prefix[right] - prefix[left]`
- 2차원에서는 겹치는 영역을 한 번 빼고 다시 더해줘야 함
- 누적합은 **계산을 미리 당겨서** 쿼리 속도를 빠르게 만드는 방식

### 실수 포인트 ⚠️
- 인덱스 혼동
- `left`, `right` 범위 정의 실수
- 2차원에서 중복 영역 처리 누락

</details>

---

## 📌 Hash / Dictionary

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
값의 등장 횟수를 저장하거나, 특정 값을 빠르게 조회하기 위한 자료구조

### 핵심 아이디어
- 배열로 전부 탐색하면 O(N)이지만, 딕셔너리를 쓰면 평균 O(1)에 조회 가능
- **값 자체보다 빈도, 존재 여부, 매핑 관계**가 중요할 때 강력하다.

### 기본 카운팅 예시
```python
arr = [1, 2, 2, 3, 3, 3]

count = {}
for x in arr:
    count[x] = count.get(x, 0) + 1

print(count)      # {1: 1, 2: 2, 3: 3}
print(count[2])   # 2
```

### 두 수의 합 존재 여부 예시
```python
arr = [2, 7, 11, 15]
target = 9

seen = set()

for num in arr:
    if target - num in seen:
        print("found")
        break
    seen.add(num)
```

### 부분합 + 해시 예시
```python
# 누적합이 같은 구간을 찾는 대표 패턴
arr = [1, -1, 2, -2, 3]

prefix = 0
count = {0: 1}
answer = 0

for x in arr:
    prefix += x
    answer += count.get(prefix, 0)
    count[prefix] = count.get(prefix, 0) + 1

print(answer)
```

### 언제 쓰나?
- 빈도수 카운팅
- 빠른 검색
- 중복 제거
- 부분합 / 투썸 / 조합 카운팅

### 핵심 포인트 🔥
- `dict.get(key, 0)` 패턴 자주 사용
- 존재 여부만 필요하면 `set`도 좋음
- 부분합과 결합하면 경우의 수 문제에 매우 강력함

### 실수 포인트 ⚠️
- 없는 key 접근
- 카운트 초기값 누락
- `set`과 `dict` 역할 혼동

</details>

---

## 📌 Two Pointer

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
배열 양 끝이나 두 위치를 가리키는 포인터를 움직이며 탐색하는 기법

### 핵심 아이디어
- 정렬된 상태에서 조건에 따라 포인터 이동 방향이 결정된다.
- O(N²) 탐색을 O(N) 혹은 O(N log N) 수준으로 줄이는 대표 기법

### 양쪽 끝에서 합 찾기
```python
arr = [1, 2, 3, 4, 5]
target = 6

left, right = 0, len(arr) - 1

while left < right:
    current = arr[left] + arr[right]

    if current == target:
        print(left, right)   # 0, 4
        break
    elif current < target:
        left += 1
    else:
        right -= 1
```

### 연속 부분합 예시
```python
arr = [1, 2, 3, 2, 5]
target = 5

left = 0
current_sum = 0
count = 0

for right in range(len(arr)):
    current_sum += arr[right]

    while current_sum > target:
        current_sum -= arr[left]
        left += 1

    if current_sum == target:
        count += 1

print(count)
```

### 좋은 수 / 조합 검사 패턴
```python
arr = sorted([1, 2, 3, 4, 5])
target_index = 3   # 값 4를 두 수의 합으로 만들 수 있는지 검사

target = arr[target_index]
left, right = 0, len(arr) - 1

while left < right:
    if left == target_index:
        left += 1
        continue
    if right == target_index:
        right -= 1
        continue

    s = arr[left] + arr[right]
    if s == target:
        print(True)
        break
    elif s < target:
        left += 1
    else:
        right -= 1
```

### 언제 쓰나?
- 정렬된 배열의 합 문제
- 연속 구간 문제
- 특정 조건을 만족하는 쌍 / 구간 탐색

### 핵심 포인트 🔥
- 합 비교형이면 보통 정렬 후 양끝 포인터
- 연속 구간형이면 슬라이딩 윈도우처럼 사용
- 조건에 따라 어느 포인터를 움직일지 명확해야 함

### 실수 포인트 ⚠️
- 정렬 안 하고 사용
- `left < right` 조건 실수
- 자기 자신을 사용하는 경우 처리 누락

</details>

---

## 📌 Binary Search (이분 탐색)

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
정렬된 데이터에서 탐색 범위를 절반씩 줄이며 원하는 값을 찾는 방법

### 핵심 아이디어
- 탐색 범위가 절반씩 줄어들기 때문에 O(log N)
- "정답의 범위"를 탐색하는 **파라메트릭 서치**에도 자주 사용된다.

### 기본 이분 탐색
```python
arr = [1, 3, 5, 7, 9]
target = 7

left, right = 0, len(arr) - 1
found = False

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(found)
```

### lower bound 스타일
```python
arr = [1, 2, 2, 2, 3, 4]
target = 2

left, right = 0, len(arr)

while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid

print(left)   # 첫 번째 2의 위치
```

### 파라메트릭 서치 예시
```python
# 랜선 자르기 느낌
arr = [802, 743, 457, 539]
target_count = 11

left, right = 1, max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    pieces = sum(x // mid for x in arr)

    if pieces >= target_count:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
```

### 언제 쓰나?
- 정렬된 배열에서 값 찾기
- 특정 기준을 만족하는 최소/최대값 찾기
- 파라메트릭 서치

### 핵심 포인트 🔥
- `left <= right` 와 `left < right` 구분
- 탐색 대상이 값인지, 정답 범위인지 먼저 판단
- 파라메트릭 서치는 "이 길이가 가능하냐?" 같은 판정 함수가 중요

### 실수 포인트 ⚠️
- mid 계산 후 구간 갱신 오류
- lower bound / upper bound 혼동
- 정렬 전제 놓침

</details>

---

## 📌 Dynamic Programming (DP)

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
작은 문제의 답을 이용해 큰 문제를 해결하는 기법

### 핵심 아이디어
- 같은 상태를 여러 번 계산하지 않도록 저장한다.
- 핵심은 **상태 정의**와 **점화식**이다.

### 1차원 DP 예시 (피보나치)
```python
n = 7

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
```

### 0/1 배낭 예시
```python
k = 7
items = [(3, 4), (4, 5), (2, 3)]

dp = [0] * (k + 1)

for w, v in items:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])
```

### 메모이제이션 예시
```python
memo = {}

def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(7))
```

### 언제 쓰나?
- 같은 상태가 반복됨
- 최댓값 / 최솟값 / 경우의 수
- 이전 상태를 기반으로 현재 상태가 정해짐

### 핵심 포인트 🔥
- `dp[i]`가 무엇인지 문장으로 정의할 수 있어야 함
- 점화식은 "현재 상태가 이전 상태에서 어떻게 오는가"
- 배낭 문제는 순회 방향이 매우 중요

### 실수 포인트 ⚠️
- 상태 정의 불명확
- 점화식 오류
- 초기값 설정 누락
- 순회 방향 반대로 돌림

</details>

---

## 📌 DFS / BFS

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
그래프 / 트리 / 격자에서 탐색하는 기본 알고리즘

### 핵심 아이디어
- DFS: 깊게 들어가며 탐색
- BFS: 가까운 것부터 넓게 탐색

### DFS 예시
```python
graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

visited = {1: False, 2: False, 3: False, 4: False}

def dfs(node):
    visited[node] = True
    print(node)

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)
```

### BFS 예시
```python
from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

visited = {1: False, 2: False, 3: False, 4: False}

queue = deque([1])
visited[1] = True

while queue:
    node = queue.popleft()
    print(node)

    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            queue.append(nxt)
```

### 격자 BFS 예시
```python
from collections import deque

board = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

n, m = 3, 3
visited = [[False] * m for _ in range(n)]
directions = [(-1,0), (1,0), (0,-1), (0,1)]

queue = deque([(0, 0)])
visited[0][0] = True

while queue:
    x, y = queue.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
```

### 언제 쓰나?
- 연결 요소 찾기
- 경로 탐색
- 그래프 순회
- 격자 문제

### 핵심 포인트 🔥
- DFS는 백트래킹과 잘 연결됨
- BFS는 무가중치 최단거리에서 강력
- `visited` 처리 위치가 중요

### 실수 포인트 ⚠️
- visited 누락
- 재귀 깊이 초과
- BFS에서 방문 처리 늦게 해서 중복 삽입

</details>

---

## 📌 Dijkstra

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
가중치가 있는 그래프에서 최단 거리를 구하는 알고리즘

### 핵심 아이디어
- 현재까지 가장 가까운 노드부터 확정해나간다.
- 우선순위 큐를 사용하면 O(E log V)로 처리 가능

### 기본 예시
```python
import heapq

n = 5
graph = {
    1: [(2, 2), (5, 3)],
    2: [(3, 4), (4, 5)],
    3: [(4, 6)],
    4: [],
    5: [(4, 2)]
}

start = 1
dist = [float('inf')] * (n + 1)
dist[start] = 0

heap = [(0, start)]

while heap:
    cost, node = heapq.heappop(heap)

    if cost > dist[node]:
        continue

    for next_cost, next_node in graph[node]:
        new_cost = cost + next_cost
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))

print(dist[1:])   # [0, 2, 6, 5, 3]
```

### 경로 복원 예시
```python
import heapq

n = 4
graph = {
    1: [(2, 1), (3, 4)],
    2: [(3, 2), (4, 5)],
    3: [(4, 1)],
    4: []
}

start = 1
dist = [float('inf')] * (n + 1)
prev = [-1] * (n + 1)
dist[start] = 0

heap = [(0, start)]

while heap:
    cost, node = heapq.heappop(heap)

    if cost > dist[node]:
        continue

    for weight, nxt in graph[node]:
        new_cost = cost + weight
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            prev[nxt] = node
            heapq.heappush(heap, (new_cost, nxt))

target = 4
path = []

while target != -1:
    path.append(target)
    target = prev[target]

path.reverse()
print(path)   # [1, 2, 3, 4]
```

### 언제 쓰나?
- 가중치 있는 최단거리
- 시작점에서 모든 정점까지 거리
- 경로 복원 문제

### 핵심 포인트 🔥
- 음수 간선이 있으면 안 됨
- `if cost > dist[node]: continue` 중요
- BFS와 구분: 가중치가 있으면 다익스트라 고려

### 실수 포인트 ⚠️
- 우선순위 큐에 `(노드, 비용)` 순서로 넣는 실수
- dist 갱신 조건 누락
- 음수 간선 문제에 사용

</details>

---

## 📌 Topological Sort

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
선후 관계가 있는 작업들을 올바른 순서대로 나열하는 알고리즘

### 핵심 아이디어
- 진입차수(indegree)가 0인 노드부터 처리
- DAG(사이클이 없는 방향 그래프)에서만 가능

### 기본 예시
```python
from collections import deque

n = 4
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

indegree = [0] * (n + 1)
for node in graph:
    for nxt in graph[node]:
        indegree[nxt] += 1

queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    node = queue.popleft()
    result.append(node)

    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(result)
```

### 우선순위 큐 버전 예시
```python
import heapq

n = 4
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

indegree = [0] * (n + 1)
for node in graph:
    for nxt in graph[node]:
        indegree[nxt] += 1

heap = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    node = heapq.heappop(heap)
    result.append(node)

    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)

print(result)
```

### 언제 쓰나?
- 선수 과목 문제
- 작업 순서 정하기
- 의존성 처리

### 핵심 포인트 🔥
- indegree 배열이 핵심
- 큐를 쓰면 일반 위상정렬
- 힙을 쓰면 번호가 작은 것부터 선택 가능

### 실수 포인트 ⚠️
- 방향 반대로 그래프 구성
- indegree 계산 누락
- 사이클 존재 시 처리 불가

</details>

---

## 📌 Backtracking (백트래킹)

<details>
<summary>📖 개념 + 예시 + 핵심 포인트 보기</summary>

<br>

### 개념
가능한 경우를 탐색하되, 조건에 맞지 않으면 더 깊게 가지 않고 되돌아오는 방식

### 핵심 아이디어
- DFS 기반 탐색 + 가지치기
- "이 경로는 더 볼 필요가 없다"를 빨리 판단하는 게 중요

### 순열 예시
```python
arr = [1, 2, 3]
visited = [False] * len(arr)
path = []

def backtrack():
    if len(path) == len(arr):
        print(path)
        return

    for i in range(len(arr)):
        if visited[i]:
            continue

        visited[i] = True
        path.append(arr[i])

        backtrack()

        path.pop()
        visited[i] = False

backtrack()
```

### N-Queen 느낌의 가지치기 예시
```python
n = 4
cols = [False] * n
diag1 = [False] * (2 * n)
diag2 = [False] * (2 * n)
count = 0

def dfs(row):
    global count
    if row == n:
        count += 1
        return

    for col in range(n):
        if cols[col] or diag1[row + col] or diag2[row - col + n]:
            continue

        cols[col] = diag1[row + col] = diag2[row - col + n] = True
        dfs(row + 1)
        cols[col] = diag1[row + col] = diag2[row - col + n] = False

dfs(0)
print(count)
```

### 언제 쓰나?
- 순열 / 조합
- 모든 경우 탐색
- 조건 만족 여부 검사

### 핵심 포인트 🔥
- 상태를 선택 → 재귀 → 원복
- 가지치기 조건이 성능을 좌우함
- DFS와 비슷하지만, 조건에 따라 탐색을 끊는 것이 핵심

### 실수 포인트 ⚠️
- 원복 누락
- 종료 조건 누락
- 불필요한 중복 탐색

</details>

---

# 🧩 Common Patterns

<details>
<summary>📖 자주 쓰는 실전 패턴 보기</summary>

<br>

### 1. 부분합 + 해시
```python
arr = [1, 1, 1]
target = 2

prefix = 0
count = {0: 1}
answer = 0

for x in arr:
    prefix += x
    answer += count.get(prefix - target, 0)
    count[prefix] = count.get(prefix, 0) + 1

print(answer)
```

### 2. 정렬 + 투포인터
```python
arr = sorted([5, 1, 3, 2, 4])

left, right = 0, len(arr) - 1
while left < right:
    print(arr[left], arr[right])
    left += 1
    right -= 1
```

### 3. BFS 최단거리 템플릿
```python
from collections import deque

dist = [-1] * n
queue = deque([start])
dist[start] = 0

while queue:
    node = queue.popleft()
    for nxt in graph[node]:
        if dist[nxt] == -1:
            dist[nxt] = dist[node] + 1
            queue.append(nxt)
```

### 4. DP 상태 정의 습관
```python
# dp[i] = i번째까지 고려했을 때의 최대값
# dp[i][j] = i번째까지 고려했을 때 j 상태의 최적값
```

</details>

---

# 🔥 Summary

- **Prefix Sum** → 구간합 최적화
- **Hash** → 빠른 조회와 카운팅
- **Two Pointer** → 정렬 후 탐색 최적화
- **Binary Search** → 절반씩 줄이며 탐색
- **DP** → 중복 계산 제거
- **DFS / BFS** → 그래프 / 격자 탐색
- **Dijkstra** → 가중치 최단 거리
- **Topological Sort** → 선후 관계 처리
- **Backtracking** → 모든 경우 탐색 + 가지치기

---

# 🎯 Goal

> 문제를 보면 어떤 알고리즘을 써야 할지 바로 떠오르고,  
> 왜 그 알고리즘을 선택해야 하는지 설명할 수 있는 수준
