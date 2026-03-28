"""
조건 
1. a(i) = a(j) + a(k) (i, j, k는 서로 다른 양의 정수) => a(i)는 좋은 수이다.
2. 수의 위치가 다르면 값이 같아도 다른 수이다. => 중복된 수가 있을 수 있다.

순서
1. 입력 받기 (첫째 줄은 수의 갯수 두번째 줄은 수의 베열)
2. 배열 정렬
3. toPointSum 함수 만들어서 두개의 합이 리스트 안에 있는지 확인(리턴값은 bool이며 True가 발생하면 바로 함수 탈출 brake)
4. 두 수의 합이 현재 값보다 작으면 왼쪽 값을 오른쪽으로 한칸 이동 크면 오른쪽 값을 왼쪽으로 한칸 이동
5. 위 함수의 값이 true면 Good의 값 +1 False면 +0
6. 모든 배열을 돌면 종료

"""
import sys
input = sys.stdin.readline

#arr[target_idx]가 다른 두 요소의 합으로 나타낼 수 있는지 확인
def toPointSum(arr, target_idx, target_val):

    left, right = 0, len(arr) - 1

    while left < right:
        # target_idx는 제외하고 다른 두 인덱스만 사용
        if left == target_idx:
            left += 1
        if right == target_idx:
            right -= 1
        
        if left >= right:
            break
            
        current_sum = arr[left] + arr[right]
        
        if current_sum == target_val:
            return True
        elif current_sum < target_val:
            left += 1
        else:
            right -= 1
    
    return False


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr_sorted = sorted(arr)
    
    good_count = 0
    
    # 각 요소에 대해 다른 두 요소의 합으로 나타낼 수 있는지 확인
    for i in range(n):
        if toPointSum(arr_sorted, i, arr_sorted[i]):
            good_count += 1
    
    print(good_count)


if __name__ == "__main__":
    main()
