class Calculator:
    def add(self,num1,num2):
        return num1 + num2
    
    def sub(self,num1,num2):
        return num1 - num2
    
    def mul(self,num1,num2):
        return num1 * num2
    
    def div(self,num1,num2):
        return num1 / num2

    def mod(self,num1,num2):
        return num1 % num2   
    
if __name__ == "__main__":
    s = Calculator()
    print("Please select operator -\n" \
        "1. Add --> +\n" \
        "2. Subtract --> -\n" \
        "3. Multiply --> *\n" \
        "4. Divide --> /\n" \
        "5. modulo --> %\n"\
        "6. Exit -->Q\n")
    
    while(True):
        f = True
        op = input("enter opration: ").strip()
        if op == "Q" or op == "q":
            print("Exit....")
            break
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        result = ""
        if op == "+":
            result = s.add(num1,num2)
        elif op == "-":
            result = s.sub(num1,num2)
        elif op == "*":
            result = s.mul(num1,num2)
        elif op == "/":
            result = s.div(num1,num2)
        elif op == "%":
            result = s.mod(num1,num2)
        else:
            print("Sorry, invalid opration.")
            f = False
        if(f):
            print(f"{num1} {op} {num2} = {result}\n")



