import shutil
def main():
    print("Enter the name of existing file: ")
    name = input()
    f=open(name,"r")
    print("Existing file:",f)
    print("Enter the file name that you want to create:")
    newname = input()
    fd = open(newname,"x")
    print("file get created with the formation as:", fd)
    shutil.copyfile(name,newname)
    #with open(name,"r")as f,open(newname,"w")as fd:
        #for line in f:
            #fd.write(line)
if __name__=="__main__":
    main()