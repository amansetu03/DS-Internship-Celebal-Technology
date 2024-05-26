def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            words = data.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."
    
file_path = 'SampleTxt.txt'
total_words = count_words(file_path)
print(f"Total number of words in '{file_path}': {total_words}")