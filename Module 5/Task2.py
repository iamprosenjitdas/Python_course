fileLoc=input("Enter the file location")

with open(fileLoc,"w") as file1:
    data=input("Enter text to write to the file:")
    writeFile= file1.writelines(data+"\n")

with open(fileLoc,"a") as file1:
    data=input("Enter additional text to append to the file:")
    appendFile=file1.writelines(data)

with open(fileLoc,"r+") as file1:
    readFile=file1.readlines()
    print(readFile)