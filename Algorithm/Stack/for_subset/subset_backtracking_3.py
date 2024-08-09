def find_subsets(depth, current_subset, current_sum):
    # 현재 부분집합의 합이 target_sum과 일치하면 result에 추가
    if current_sum == target_sum:
        result.append(current_subset[:])
        return
    
    # 현재 부분집합의 합이 target_sum을 초과하면 백트래킹
    # 백트래킹을 하지 않았을 때는 지수 시간복잡도를 갖는다.
    if current_sum > target_sum:
        return

    # 모든 수에 대해서 부분집합 생성 여부를 확인했다면 반환
    if depth == len(nums):
        return

    num = nums[depth]

    # 현재 수를 선택한 경우
    find_subsets(depth + 1, current_subset + [num], current_sum + num)

    # 현재 수를 선택하지 않는 경우
    find_subsets(depth + 1, current_subset, current_sum)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []
find_subsets(depth=0, current_subset=[], current_sum=0)

print(result)