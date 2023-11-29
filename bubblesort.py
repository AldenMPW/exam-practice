
def bubblesortv1(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list

print(bubblesortv1([6,5,4,3,2,1]))

def bubblesortv2(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i ):
            if list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list

print(bubblesortv2([6,5,4,3,2,1]))