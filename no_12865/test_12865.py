import sys

def knapsack(k, items):
    # max_value_by_capacity[c] = 허용 무게가 c일 때 가능한 최대 가치
    max_value_by_capacity = [0] * (k + 1)

    # 물건을 하나씩 보면서 "넣을지 / 안 넣을지"를 결정한다.
    for item_weight, item_value in items:
        # 0/1 배낭이므로 같은 물건이 중복 사용되지 않게 역순으로 순회한다.
        for current_capacity in range(k, 0, -1):
            # 현재 물건을 넣을 수 없는 용량이면 건너뛴다.
            if current_capacity < item_weight:
                continue

            # 1) 현재 물건을 넣지 않는 경우
            value_without_item = max_value_by_capacity[current_capacity]

            # 2) 현재 물건을 넣는 경우
            remain_capacity = current_capacity - item_weight
            value_with_item = max_value_by_capacity[remain_capacity] + item_value

            # 두 경우 중 더 큰 가치를 선택한다.
            if value_with_item > value_without_item:
                max_value_by_capacity[current_capacity] = value_with_item

    return max_value_by_capacity[k]

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    print(knapsack(k, items))