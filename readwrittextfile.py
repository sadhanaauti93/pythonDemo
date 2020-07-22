#file = open('test.txt')
#Read all the content of file
#print(file.read(5))

#file.(readline())
#file.(readline())
#print.close()

#print line by line using readline method
#line = file.readline()
#while line!="":
#print(line)
#line = filr.readline()
#readfile
line = [abc, bsdvs, "cat", dog, elephant]
for line in file.readlines():
    print(line)

    #writefile

    with open('test.txt', 'r') as reader:
        content = reader.readlines()
        reversed(content)
        with open('test.txt', 'w') as writer:
            for line in reversed(content):
                writer.write(line)

        