def reverseString(string: str) -> str:
    result = ""
    for i in range(len(string)-1,-1,-1):
        result += string[i]
    return result

def main():
    string = input("Enter String: ")
    revString = reverseString(string)
    print(f"Original string: {string}\nreversed String: {revString}")

if __name__ == "__main__":
    main()