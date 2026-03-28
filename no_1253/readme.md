# BOJ 1253 - 좋다

## 문제 요약
수열에서 어떤 값이 서로 다른 두 인덱스의 합으로 표현될 수 있으면 그 값을 GOOD이라고 한다.
주어진 N개의 수 중 GOOD인 수의 개수를 구한다.

핵심 조건:
- 인덱스가 달라야 한다. (i, j, k 서로 달라야 함)
- 값이 같아도 위치가 다르면 다른 수로 취급한다.

## 입력
- 첫 줄: N (1 <= N <= 2000)
- 둘째 줄: 정수 N개 A1 ... AN (|Ai| <= 1,000,000,000)

## 출력
- GOOD 수의 개수

## 풀이 아이디어
정렬 + 투 포인터를 사용한다.

1. 배열을 정렬한다.
2. 각 원소를 target으로 고정한다.
3. left=0, right=N-1에서 시작해 arr[left] + arr[right]를 비교한다.
4. left 또는 right가 target의 인덱스와 같으면 건너뛴다.
5. 합이 target과 같으면 해당 수는 GOOD이다.

이 방법을 모든 target에 대해 반복한다.

## 알고리즘
1. arr를 오름차순 정렬한다.
2. good_count = 0
3. 각 인덱스 i에 대해:
	 - left=0, right=N-1
	 - while left < right:
		 - if left == i: left += 1
		 - if right == i: right -= 1
		 - if left >= right: break
		 - s = arr[left] + arr[right]
		 - s == arr[i] 이면 good_count += 1 후 종료
		 - s < arr[i] 이면 left += 1
		 - s > arr[i] 이면 right -= 1
4. good_count 출력

## 시간 복잡도
- 정렬: O(N log N)
- 각 원소마다 투 포인터: O(N)
- 전체: O(N^2)

N <= 2000이므로 O(N^2)로 충분히 통과 가능하다.

## 주의할 점
- target 본인 인덱스를 합에 사용하면 안 된다.
- 중복 값이 있어도 인덱스가 다르면 사용할 수 있다.
- 음수/0/양수가 섞여 있어도 정렬 + 투 포인터로 처리 가능하다.

## 예제
입력
10
1 2 3 4 5 6 7 8 9 10

출력
8

설명
3, 4, 5, 6, 7, 8, 9, 10이 GOOD이다.