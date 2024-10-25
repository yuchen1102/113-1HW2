def missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2 
    array_sum = sum(nums) #計算數組內總和
    return total_sum - array_sum 

# 測試範例
print(missing_number([3, 0, 1]))  # 輸出: 2
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 輸出: 8