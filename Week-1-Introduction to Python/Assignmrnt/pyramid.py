
def createPyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end = " ")
        for j in range(1, 2 * i):
            print("*", end=" ")
        print()

        
if __name__ == "__main__":
    n = int(input("Enter number of row: "))
    createPyramid(n)