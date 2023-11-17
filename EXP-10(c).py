with open("test.txt") as f:
    with open("out.txt","w") as fl:
        for line in f:
            fl.write(line)