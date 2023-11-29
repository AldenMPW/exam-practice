"""
[4,3,5,6,2,1]   pivot = 4
[4][3,5,6,2,1] 
[3,2,1][4][5,6]     pivots = 3 and 5
[2,1][3][4][5][6]   pivot = 2
[1][2][3][4][5][6]
"""
def split(list,start,end):
    pivot = list[start]
    left = start + 1
    right = end
    done = False
    while done == False:
        while (left <= right) and (list[left] <= pivot):
            left += 1
            print("left:"+str(left))
        while (right >= left) and (list[right] >= pivot):
            right -= 1
            print("right:"+str(right))
        if right < left:
            done = True
        else:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp
    temp = list[right]
    list[right] = list[start]
    list[start] = temp
    return right




def quicksort(list,start,end):
    if start < end:
        splitPosition = split(list,start,end)
        list = quicksort(list,start,splitPosition-1)
        list = quicksort(list,splitPosition+1,end)
    return list

print(quicksort([3,1,2],0,2))


