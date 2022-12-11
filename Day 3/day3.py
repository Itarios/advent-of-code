from string import ascii_lowercase, ascii_uppercase, ascii_letters

# Priority value
def priority_val(letter):
    if letter not in ascii_letters:
        raise ValueError

    if letter in ascii_lowercase:
        return ord(letter)-96
    return ord(letter)-38

def find_duplicate(line):
    n=len(line)//2
    return sum([ priority_val(l) for l in line[:n] if l in line[n:]])

if __name__ == "__main__":
    # f = open("input", "r")
    f = open("test", "r")
    score=0
    for line in f:
        score+=find_duplicate(line)
    
    print(score)