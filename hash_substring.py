# python3

def read_input():
    command = input()
    if "F" in command:
        path = "tests/" + "06"
        if not "a" in file_name:
            choice = open(path, "r").read()
            partitioned = choice.partition("\n")
            choice.close()
            pattern = partitioned[0].rstrip()
            text = partitioned[2].rstrip()
            tup = tuple((pattern, text))
            return tup
        
        
    elif "I" in command:
        pattern = input().rstrip()
        text = input().rstrip()
        tup = tuple((pattern, text))
        return tup
    

def print_occurrences(output):
    print(' '.join(map(str, output)))

    
def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    result = []
    p_length = len(pattern)
    t_length = len(text)
    
    h = 1
    q = 13
    d = 256
    hashed_pattern = 0
    hashed_text = 0
    
    for i in range(p_length-1):
        h = (h * d) % q
        
    for i in range(p_length):
        hashed_pattern = (hashed_pattern * d + ord(pattern[i])) % q
        hashed_text = (hashed_text * d + ord(text[i])) % q
        
    for i in range(t_length - p_length + 1):
        if hashed_text == hashed_pattern:
            j = 0
            while j < p_length:
                if not text[i+j] == pattern[j]:
                    break
                j += 1
                
            if j == p_length:
                result.append(i)
        else:
            hashed_text = ((hashed_text - ord(text[i]) * h) * d + ord(text[i + p_length])) % q
            if hashed_text < 0:
                hashed_text += q
    # and return an iterable variable
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

