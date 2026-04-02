import sys


def solve_case(n: int, m: int) -> tuple[int, int]:
    a = min(n, m)
    b = max(n, m)

    # Case 1: two types have the same count
    if a == b:
        return a, 3

    # Case 2: k = a is enough
    if b <= 2 * a:
        return a, 7

    # Case 3: k must be a + 1
    k = a + 1

    if b <= a + 2:
        return k, 5
    if b <= 2 * a + 2:
        return k, 7

    return k, 2 * b - 4 * a + 3


def main():
    input = sys.stdin.readline
    t = int(input().strip())
    answers = []

    for _ in range(t):
        n, m = map(int, input().split())
        k, moves = solve_case(n, m)
        answers.append(f"{k} {moves}")

    print("\n".join(answers))


if __name__ == "__main__":
    main()