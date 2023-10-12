import sys 

words = dict()
nums = dict()

def __main__(): 
    for line in sys.stdin: 
        argz = line.split() 

        if argz[0] == "def":
            word = argz[1]
            num = int(argz[2])

            prevnum = words.get(word) 
            nums.pop(prevnum, None)
            words[word] = num 
            nums[num] = word

        elif argz[0] == "calc": 
            sum_ = None 
            if argz[1] in words: 
                sum_ = words[argz[1]]
                sum_ = calculate(sum_, argz[2:])

            if sum_ is not None and sum_ in nums: 
                sumstr = nums[sum_] 
            else: 
                sumstr = "unknown" 

            print(line[4:].strip(), sumstr) 

        elif argz[0] == "clear": 
            words.clear()
            nums.clear()


def calculate(sum_, argz): 
    if argz[0] == "=": 
        return sum_

    operation = argz[0]
    y = argz[1]

    if y in words: 
        y = words[y]
        #print (">", sum_, operation, y) 
        if operation=="-":
            sum_ -= y
        else: 
            sum_ += y
        return calculate(sum_, argz[2:])
    else: 
        return None


__main__()
