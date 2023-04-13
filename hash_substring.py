# python3

def read_input():
    command = input()
    if "F" in command:
        file_name = input()
        path = "tests/" + file_name
        if not "a" in file_name:
            choice = open(path, "r").read()
            partitioned = choice.partition("\n")
            choice.close()
            pattern = partitioned[0].rstrip()
            text = partitioned[2].rstrip()
            tuple = tuple(pattern, text)
            return tuple
        
        
    elif "I" in command:
        pattern = input().rstrip()
        text = input().rstrip()
        tuple = tuple(pattern, text)
        return tuple
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

    
def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    
    
    for ch in text:
        if ch == 
    # and return an iterable variable
    return [0]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

