def main():
    #list of binary search should be sorted
    list_of_evennumbers = []
    for i in range(1,101):
            list_of_evennumbers.append(i)
    target = int(input("Enter the target: "))
    
    #binary search function should return the index of the target and the number of steps to find the target
    index, steps = binary_search(list_of_evennumbers,target)
    if index != None:
        print("The Target {} taked {} to be found".format(target,steps))
    else :
        print("The Target {} doesn't exist".format(target))
def binary_search(list, target):
    counter = 0
    first = 0
    last = len(list) - 1
    while last >= first:
        middle = (last + first)//2
        counter += 1
        if list[middle] == target:
            return (middle,counter)
        elif list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    return None
            
if __name__ == "__main__":
    main()