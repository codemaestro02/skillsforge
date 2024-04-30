def printLargest(array):
    # let result = the largest of the first and second numbers in string
    result = str(max(int(array[0] + array[1]),int(array[1] + array[0])))
    for i in range(2, len(array)):
        # let result = the largest of the concatenation of the former result and the following number
        result = str(max(int(result + array[i]), int(array[i] + result)))
    
    return result


