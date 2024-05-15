
def createUpperTringle(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print("")
        
if __name__ == "__main__":
    n = int(input("Enter number of row: "))
    createUpperTringle(n)