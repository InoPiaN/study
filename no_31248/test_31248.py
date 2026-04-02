import sys


DESTINATION_PEG = "D"


def move_hanoi_three_pegs(disk_count, source_peg, target_peg, auxiliary_peg, move_list):
	if disk_count == 0:
		return

	move_hanoi_three_pegs(
		disk_count - 1,
		source_peg,
		auxiliary_peg,
		target_peg,
		move_list,
	)
	move_list.append(f"{source_peg} {target_peg}")
	move_hanoi_three_pegs(
		disk_count - 1,
		auxiliary_peg,
		target_peg,
		source_peg,
		move_list,
	)


def move_absorbing_four_pegs(disk_count, source_peg, stack_peg, single_peg, move_list):
	if disk_count == 0:
		return
	if disk_count == 1:
		move_list.append(f"{source_peg} {DESTINATION_PEG}")
		return

	# Keep the (disk_count-2) smaller disks stacked on stack_peg,
	# then move the two largest disks to D in order.
	move_hanoi_three_pegs(
		disk_count - 2,
		source_peg,
		stack_peg,
		single_peg,
		move_list,
	)
	move_list.append(f"{source_peg} {single_peg}")
	move_list.append(f"{source_peg} {DESTINATION_PEG}")
	move_list.append(f"{single_peg} {DESTINATION_PEG}")

	move_absorbing_four_pegs(
		disk_count - 2,
		stack_peg,
		source_peg,
		single_peg,
		move_list,
	)


def main():
	input_data = sys.stdin.buffer.readline
	disk_count = int(input_data().strip())

	moves = []
	move_absorbing_four_pegs(disk_count, "A", "C", "B", moves)

	output_lines = [str(len(moves))]
	output_lines.extend(moves)
	sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
	main()
