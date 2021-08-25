lines = ["Hi", "Hi2", "Hi3"]
with open("test.txt", "r+") as File:
    #for line in lines:
        #line = line + "\n"
        #print(line)
        #File.write(line)
    print(File.read())