f = open("demofile2.txt", "a")
f.write("100\n")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()

with open("counter.txt", "w") as f:
    for i in range (1, 101):
        f.write(str(i) + '\n')

    

