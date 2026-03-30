import sys


def count_odd_numbers(limit):
    return (limit + 1) // 2


def solve(n, k):
    # 2^60 > 10^18 이므로 K가 61 이상이면 항상 불가능
    if k > 60:
        return 0

    power_of_2_k = 1 << k
    if power_of_2_k > n:
        return 0

    max_odd = n // power_of_2_k
    return count_odd_numbers(max_odd)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    test_cases = data[0]

    results = []
    index = 1
    for _ in range(test_cases):
        n = data[index]
        k = data[index + 1]
        index += 2
        results.append(str(solve(n, k)))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()
