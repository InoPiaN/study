import sys


def build_subarray_sums(numbers):
	subarray_sums = []
	length = len(numbers)

	for start_index in range(length):
		running_sum = 0
		for end_index in range(start_index, length):
			running_sum += numbers[end_index]
			subarray_sums.append(running_sum)

	return subarray_sums


def main():
	input_stream = sys.stdin.readline

	target_sum = int(input_stream().strip())

	array_a_length = int(input_stream().strip())
	array_a = list(map(int, input_stream().split()))

	array_b_length = int(input_stream().strip())
	array_b = list(map(int, input_stream().split()))

	subarray_sums_a = build_subarray_sums(array_a)
	subarray_sums_b = build_subarray_sums(array_b)

	sum_count_in_b = {}
	for subarray_sum_b in subarray_sums_b:
		if subarray_sum_b in sum_count_in_b:
			sum_count_in_b[subarray_sum_b] += 1
		else:
			sum_count_in_b[subarray_sum_b] = 1

	pair_count = 0
	for subarray_sum_a in subarray_sums_a:
		required_sum = target_sum - subarray_sum_a
		pair_count += sum_count_in_b.get(required_sum, 0)

	print(pair_count)


if __name__ == "__main__":
	main()
