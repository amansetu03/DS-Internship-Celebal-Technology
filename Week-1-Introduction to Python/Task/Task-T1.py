def find_max(num1, num2, num3): 
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

def main():
    print("Enter three number: ")
    num1,num2,num3 = [int(x) for x in input().split()]
    largesNumber = find_max(num1, num2, num3)
    print(f"largest number -> {largesNumber}")

if __name__ == "__main__":
    main()