# 1. return first repeat occurence Element index
"""-> output = 5"""

arr = [10,4,5,3,5,3,6]

for num in arr:
    if arr.count(num) > 1:
        print(num)
        break

