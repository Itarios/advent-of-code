
def all_different(a,b,c,d):
    return abs((a-b)*(a-c)*(a-d)*(b-c)*(b-d)*(c-d))

def all_different_list(lista):
    while(lista):
        if( lista.pop() in lista ):
            return False
    return True

def  start_of_packet_marker(buffer):
    n=len(buffer)
    
    for i in range(4,n):
        if( all_different(*[ord(c) for c in buffer[i-4:i]]) ):
            return i

def  start_of_marker(buffer,k):
    n=len(buffer)
    
    for i in range(k,n):
        if( all_different_list( list(buffer[i-k:i]) ) ):
            return i

if __name__ == "__main__":
    f = open("input", "r")
    # f = open("test", "r")

    for line in f:
        print(start_of_marker(line,14))
