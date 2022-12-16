def main():
    fname=input("Enter name of file:")
    word=input("Enter the word to be searched:")
    k=0
    with open(fname,"r")as f:
        for line in f:
            words=line.split()
            for i in words:
                if(i==word):
                    k=k+1
    print("Occurance of the word:",k)
if __name__=="__main__":
    main()