def fileSwap():
    file1 = input("Enter the first file ->")
    file2 = input("Enter the second file ->")
    with open (file1,"r")as f:
        dataA = f.read()
    with open (file2,"r") as f2:
        dataB = f2.read()
    with open (file1,"w") as f:
        f.write(dataB)
    with open (file2,"w") as f2:
        f2.write(dataA)

fileSwap()