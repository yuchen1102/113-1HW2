from typing import List

def getResult():
    # 宣告鍵盤矩陣 alphabet1 和 alphabet2
    alphabet1: List[List[chr]] = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
    ]
    
    alphabet2: List[List[chr]] = [
        ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
    ]
    
    # 輸入測試筆數
    n = int(input("請輸入測試筆數 N: "))
    
    for _ in range(n):
        # 輸入符號和方向
        value, direction = input("請輸入 符號 和 方向 (1:上，2:下，3:右，4:左): ").split()
        direction = int(direction)
        found = False
        
        # alphabet1 來尋找 value 的位置
        for i in range(len(alphabet1)):
            if value in alphabet1[i]:
                j = alphabet1[i].index(value)
                found = True
                
                # 根據 direction 移動並在 alphabet1 中找出新位置的字符
                if direction == 1:  # 上
                    new_value = alphabet1[i-1][j]
                elif direction == 2:  # 下
                    new_value = alphabet1[i+1][j]
                elif direction == 3:  # 右
                    new_value = alphabet1[i][j+1]
                elif direction == 4:  # 左
                    new_value = alphabet1[i][j-1]
                else:
                    new_value = value
                
                print(new_value)
                break
        
        # 如果在 alphabet1 沒找到，再在 alphabet2 中查找
        if not found:
            for i in range(len(alphabet2)):
                if value in alphabet2[i]:
                    j = alphabet2[i].index(value)
                    
                    # 根據 direction 移動並找出新位置的字符
                    if direction == 1:  # 上
                        new_value = alphabet2[i-1][j]
                    elif direction == 2: # 下
                        new_value = alphabet2[i+1][j]
                    elif direction == 3: # 右
                        new_value = alphabet2[i][j+1]
                    elif direction == 4:  # 左
                        new_value = alphabet2[i][j-1]
                    else:
                        new_value = value
                    
                    print(new_value)
                    break

# 執行函式
getResult()
