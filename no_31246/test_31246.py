import sys
import heapq


def main() -> None:
	input_data = sys.stdin.readline
	ad_slot_count, target_win_count = map(int, input_data().split())

	# Keep only the smallest target_win_count values using a max-heap.
	smallest_required_increases_max_heap = []

	for _ in range(ad_slot_count):
		my_bid_price, competitor_top_bid = map(int, input_data().split())
		required_increase = max(0, competitor_top_bid - my_bid_price)
		if len(smallest_required_increases_max_heap) < target_win_count:
			heapq.heappush(smallest_required_increases_max_heap, -required_increase)
			continue

		current_kth_smallest = -smallest_required_increases_max_heap[0]
		if required_increase < current_kth_smallest:
			heapq.heapreplace(smallest_required_increases_max_heap, -required_increase)

	print(-smallest_required_increases_max_heap[0])


if __name__ == "__main__":
	main()
