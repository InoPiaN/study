import sys

def required_withdraw_count(k, expenses):
	count = 1
	balance = k

	for cost in expenses:
		if balance < cost:
			count += 1
			balance = k
		balance -= cost

	return count


def main():
	input = sys.stdin.readline

	n, m = map(int, input().split())
	expenses = [int(input()) for _ in range(n)]

	left = max(expenses)
	right = sum(expenses)
	answer = right

	while left <= right:
		mid = (left + right) // 2
		cnt = required_withdraw_count(mid, expenses)

		if cnt <= m:
			answer = mid
			right = mid - 1
		else:
			left = mid + 1

	print(answer)


if __name__ == "__main__":
	main()