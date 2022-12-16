import os
def main():
    print("Enter the file name that you want to open :")
    name=input()
    if os.path.exists(name):
        fd = open(name, 'r')
        #print(type(fd))
        data = fd.read()
        print("Data from file is:", data)
        fd.close()
if __name__=="__main__":
    main()