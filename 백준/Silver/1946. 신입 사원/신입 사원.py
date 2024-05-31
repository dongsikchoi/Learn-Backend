import sys

input = sys.stdin.readline
test_count = int(input())


for _ in range(test_count):
    test_case_count = int(input())
    grade_result = sorted([list(map(int,input().strip().split())) for _ in range(test_case_count)])
    result_count = 1
    interview_baseline_rank = grade_result[0][1]
    for i in range(1, test_case_count):
        interview_compare_target_rank = grade_result[i][1]
        if interview_compare_target_rank < interview_baseline_rank:
            result_count += 1
            interview_baseline_rank = interview_compare_target_rank
    print(result_count)
