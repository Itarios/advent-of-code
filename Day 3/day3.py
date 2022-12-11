from string import ascii_lowercase, ascii_uppercase, ascii_letters

# Priority value
def priority_val(letter):
    if letter not in ascii_letters:
        return 0
    if letter in ascii_lowercase:
        return ord(letter)-96
    return ord(letter)-38

def find_duplicate(line):
    n=len(line)//2
    return [ priority_val(item) for item in line[:n] if item in line[n:]][0]

def find_comon(line1,line2,line3):
    comon_items=set(line1).intersection(line2).intersection(line3)
    return sum( [ priority_val(item) for item in comon_items ] )

if __name__ == "__main__":
    f = open("input", "r")
    # f = open("test", "r")
    score=0
    # for line in f:
    #     score+=find_duplicate(line)

    for line1 in f:
        score+=find_comon(line1,f.readline(),f.readline())
    print(score)