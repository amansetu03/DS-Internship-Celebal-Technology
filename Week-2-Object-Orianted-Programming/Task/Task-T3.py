def calculate_sum(file_path):
    try:
        with open(file_path, 'r') as file:
            total_sum = 0
            print("Numbers:--> ",end="")
            data = file.read()
            words = data.split()
            # print(words)
            for word in  words:
                try:
                    number = int(word.strip())
                    print(number,end=", ")
                    total_sum += number
                except ValueError:
                    pass
                
            return total_sum
    except FileNotFoundError:
        return "File not found."


file_path = 'numbers.txt'
result = calculate_sum(file_path)
print(f"\nSum of numbers in '{file_path}': {result}")
