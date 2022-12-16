
def main():
    print("Enter the First file name :")
    F=input()
    f1=open(F,"r")
    print(f1)
    print("Enter the Second file name :")
    F1 = input()
    f2 = open(F1, "r")
    print(f2)
    for line1 in f1:
        for line2 in f2:
            if line1==line2:
                print("success")
            else:
                print("Failure")

            break
    f1.close()
    f2.close()

if __name__=="__main__":
    main()