import sys
import traceback

# 디버깅용 입력 데이터 하드코딩
input_data = """3 3 10
1 2 3
1 2 5
2 3 10
3 1 15"""
input = iter(input_data.splitlines()).__next__

MOD = 1_000_000_007

def solve():
    print("solve() 함수 시작", flush=True)  # 디버깅용 로그
    try:
        n, m, k = map(int, input().split())
        print(f"n={n}, m={m}, k={k}", flush=True)  # 입력 확인
        increments = list(map(int, input().split()))
        print(f"increments={increments}", flush=True)  # 입력 확인

        edges_by_b = []

        for _ in range(m):
            source, target, b_value = map(int, input().split())
            source -= 1
            target -= 1
            edges_by_b.append((b_value, source, target))

        print(f"edges_by_b={edges_by_b}", flush=True)  # 입력 확인

        edges_by_b.sort()
        sorted_b_values = [edge[0] for edge in edges_by_b]

        transitions = list(range(n))
        threshold_pointer = 0

        current_vertex = 0
        current_counter = 0
        remaining_steps = k

        max_iterations = 1000  # 최대 반복 횟수
        iterations = 0

        while remaining_steps > 0:
            iterations += 1
            if iterations > max_iterations:
                print("루프가 너무 오래 실행되어 강제 종료합니다.", flush=True)
                break

            print(f"루프 상태: remaining_steps={remaining_steps}, current_vertex={current_vertex}, current_counter={current_counter}", flush=True)
            while threshold_pointer < m and sorted_b_values[threshold_pointer] <= current_counter:
                _, source, target = edges_by_b[threshold_pointer]
                transitions[source] = target
                threshold_pointer += 1

            if threshold_pointer < m:
                next_threshold = sorted_b_values[threshold_pointer]
            else:
                next_threshold = None

            visited_index = [-1] * n
            path_vertices = [0] * (n + 1)
            prefix_sum = [0]
            path_length = 0

            walk_vertex = current_vertex
            while visited_index[walk_vertex] == -1:
                visited_index[walk_vertex] = path_length
                path_vertices[path_length] = walk_vertex
                path_length += 1

                nxt = transitions[walk_vertex]
                prefix_sum.append(prefix_sum[-1] + increments[nxt])

                walk_vertex = nxt

            cycle_start = visited_index[walk_vertex]
            total_unique = path_length
            cycle_length = total_unique - cycle_start
            cycle_sum = prefix_sum[total_unique] - prefix_sum[cycle_start]

            cycle_prefix = prefix_sum[cycle_start]

            if next_threshold is None:
                take_steps = remaining_steps
            else:
                need = next_threshold - current_counter
                if remaining_steps <= total_unique:
                    total_if_all = prefix_sum[remaining_steps]
                else:
                    after_enter = remaining_steps - cycle_start
                    full_cycles = after_enter // cycle_length
                    tail = after_enter % cycle_length
                    total_if_all = (
                        cycle_prefix
                        + full_cycles * cycle_sum
                        + (prefix_sum[cycle_start + tail] - cycle_prefix)
                    )

                if total_if_all < need:
                    take_steps = remaining_steps
                else:
                    left, right = 1, remaining_steps
                    while left < right:
                        mid = (left + right) // 2
                        if mid <= total_unique:
                            mid_increment = prefix_sum[mid]
                        else:
                            after_enter = mid - cycle_start
                            full_cycles = after_enter // cycle_length
                            tail = after_enter % cycle_length
                            mid_increment = (
                                cycle_prefix
                                + full_cycles * cycle_sum
                                + (prefix_sum[cycle_start + tail] - cycle_prefix)
                            )

                        if mid_increment >= need:
                            right = mid
                        else:
                            left = mid + 1
                    take_steps = left

            if take_steps <= total_unique:
                gained = prefix_sum[take_steps]
            else:
                after_enter = take_steps - cycle_start
                full_cycles = after_enter // cycle_length
                tail = after_enter % cycle_length
                gained = (
                    cycle_prefix
                    + full_cycles * cycle_sum
                    + (prefix_sum[cycle_start + tail] - cycle_prefix)
                )

            current_counter += gained
            if take_steps < total_unique:
                current_vertex = path_vertices[take_steps]
            else:
                after_enter = take_steps - cycle_start
                current_vertex = path_vertices[cycle_start + (after_enter % cycle_length)]

            remaining_steps -= take_steps

        print(current_vertex + 1, current_counter % MOD, flush=True)
    except Exception as e:
        print(f"에러 발생: {e}", flush=True)
        traceback.print_exc()

if __name__ == "__main__":
    print("프로그램 시작", flush=True)
    solve()
    print("프로그램 종료", flush=True)