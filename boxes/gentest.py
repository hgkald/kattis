with open("test1bigbox.in", 'w') as f: 
    f.write("200000\n")
    for i in range(200000):
        if i == 0: 
            f.write("0" + " ") 
        else:
            f.write("1" + " ") 
    f.write("\n")
    f.write("2\n")
    f.write("1 199999\n")
    f.write("1 1")
