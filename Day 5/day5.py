from re import findall 


def initial_state_input():
    stack_crates=[]

    #Add stack 1
    stack_crates.append( list("DHNQTWVB") )
    #Add stack 2
    stack_crates.append( list("DWB") )
    #Add stack 3
    stack_crates.append( list("TSQWJC") )
    #Add stack 4
    stack_crates.append( list("FJRNZTP") )
    #Add stack 5
    stack_crates.append( list("GPVJMST") )
    #Add stack 6
    stack_crates.append( list("BWFTN") )
    #Add stack 7
    stack_crates.append( list("BLDQFHVN") )
    #Add stack 8
    stack_crates.append( list("HPFR") )
    #Add stack 9
    stack_crates.append( list("ZSMBLNPH") )

    return stack_crates

def initial_state_test():
    stack_crates=[]

    #Add stack 1
    stack_crates.append( list("ZN") )
    #Add stack 2
    stack_crates.append( list("MCD") )
    #Add stack 3
    stack_crates.append( list("P") )

    return stack_crates

def crate_9000_instruction(stacks, n, stack1, stack2):
    stack1-=1
    stack2-=1

    for i in range(n):
        stacks[stack2].append( stacks[stack1].pop() )

def crate_9001_instruction(stacks, n, stack1, stack2):
    stack1-=1
    stack2-=1

    stacks[stack2].extend( stacks[stack1][-n:] )
    del stacks[stack1][-n:]

def skip_lines(f,n):
    for i in range(n):
        f.readline()

if __name__ == "__main__":
    

    f = open("input", "r")
    stacks=initial_state_input()
    skip_lines(f,10)
    
    # f = open("test", "r")
    # stacks=initial_state_test()
    # skip_lines(f,5)

    result=""

    for line in f:
        instruction=[int(i) for i in findall(r'\d+',line)]
        # crate_9000_instruction(stacks,*instruction)
        crate_9001_instruction(stacks,*instruction)
    
    for stack in stacks:
        result+=stack[-1]
    
    print(result)
