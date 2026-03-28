import sys
import heapq

def solution(problem_count, adjacency_list, indegree):
    available_problems = []
    for problem_number in range(1, problem_count + 1):
        if indegree[problem_number] == 0:
            heapq.heappush(available_problems, problem_number)

    solve_order = []
    while available_problems:
        current_problem = heapq.heappop(available_problems)
        solve_order.append(current_problem)

        for next_problem in adjacency_list[current_problem]:
            indegree[next_problem] -= 1
            if indegree[next_problem] == 0:
                heapq.heappush(available_problems, next_problem)

    return solve_order

def main():
    input = sys.stdin.readline
    problem_count, relation_count = map(int, input().split())
    adjacency_list = [[] for _ in range(problem_count + 1)]
    indegree = [0] * (problem_count + 1)

    for _ in range(relation_count):
        prerequisite_problem, target_problem = map(int, input().split())
        adjacency_list[prerequisite_problem].append(target_problem)
        indegree[target_problem] += 1

    solve_order = solution(problem_count, adjacency_list, indegree)
    print(*solve_order)



if __name__ == "__main__":
    main()