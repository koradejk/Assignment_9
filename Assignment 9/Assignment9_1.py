import os
def main():
    print("Enter the name of file that you want to check:")
    name=input()
    if os.path.isfile(name):
        print("File are found")
    else:
        print("File not found")

if __name__=="__main__":
    main()