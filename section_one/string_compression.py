def compress(string):
    count = 1
    result = ""
    for i in range(len(string) - 1):
        
        # if the element in that position is equal to the next one, add one to the count
        if string[i] == string[i + 1]:
            count += 1
            
        #if the element in that position is not equal to the next one and the count is 1, add just the letter
        elif string[i] != string[i + 1] and count == 1:
            result += string[i]
            
        # if the element in that position is not equal to the next one and count is greater than one, add the letter plus its count
        else:
            result += string[i] + str(count)
            count = 1

    return result + string[-1] + str(count)

# Test cases
assert compress("aabcccccaaa") == "a2bc5a3"
assert compress("abbccc") == "ab2c3"
assert compress("abcdee") == "abcde2"