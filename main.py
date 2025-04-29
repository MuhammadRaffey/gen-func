def read_file_lines(filepath):
    """Generator function to read a file line by line."""
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.rstrip('\n')

if __name__ == "__main__":
    for line in read_file_lines('why_chatgpt_is_best.md'):
        print(line)