## 문제 요약
두 배열 A, B가 주어질 때,

- A의 부배열 합 하나
- B의 부배열 합 하나

를 더해서 T가 되는 모든 쌍의 개수를 구하는 문제.

핵심은 "부배열"이므로 원소를 임의로 고르는 것이 아니라 연속 구간 합만 허용된다는 점이다.

## 핵심 아이디어
식을 다음처럼 본다.

sumA + sumB = T

sumA를 하나 고르면 필요한 값은 required = T - sumA 로 고정된다.
즉, A 쪽 부배열 합을 하나씩 보면서 B 쪽에서 required가 몇 번 나오는지 세면 된다.

## 알고리즘
1. A의 모든 부배열 합을 구해 리스트 subarray_sums_a에 저장
2. B의 모든 부배열 합을 구해 리스트 subarray_sums_b에 저장
3. subarray_sums_b를 딕셔너리로 빈도 집계
      - sum_count_in_b[value] = value가 나온 횟수
4. subarray_sums_a를 순회
      - required_sum = T - subarray_sum_a
      - answer += sum_count_in_b.get(required_sum, 0)

## 왜 맞는가
모든 A 부배열 합 sumA에 대해,
sumA + sumB = T를 만족하는 sumB는 정확히 T - sumA 하나뿐이다.

또한 B의 부배열 합 중 같은 값이 여러 번 나올 수 있으므로,
"존재 여부"가 아니라 "등장 횟수"를 더해야 한다.

따라서 A의 모든 경우에 대해 B의 대응 개수를 누적하면,
조건을 만족하는 (A 부배열, B 부배열) 쌍의 총개수와 정확히 일치한다.

## 복잡도
- A의 부배열 합 개수: O(n^2)
- B의 부배열 합 개수: O(m^2)
- 빈도 집계 + 조회: O(n^2 + m^2)

전체 시간복잡도: O(n^2 + m^2)

전체 공간복잡도: O(n^2 + m^2)

제한 n, m <= 1000에서 충분히 통과 가능하다.

## 구현 포인트
- 부배열 합 생성은 시작점을 고정하고 끝점을 늘리며 running_sum 누적
- 딕셔너리 조회 시 get(key, 0) 사용
  - key가 없으면 0을 반환해 KeyError 없이 누적 가능

## 참고
현재 구현 파일: test_2143.py