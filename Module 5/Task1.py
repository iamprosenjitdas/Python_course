fileLoc=input("Enter File Location")
try:
    with open(fileLoc,'r+') as file1:
        readFile = file1.readlines()
        print(readFile)
except  FileNotFoundError:
    print("The file",fileLoc,"not found")
finally:
    print("Continue with execution")