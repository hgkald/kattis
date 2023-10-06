line = input()
vals = line.split(";")
count = 0
for val in vals: 
    range_ = val.split("-")
    if len(range_) > 1: 
        count += int(range_[1])-int(range_[0])+1
    elif len(range_) == 1: 
        count += 1
print(count)


