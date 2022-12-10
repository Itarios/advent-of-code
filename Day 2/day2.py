# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors



Val={"X":1, "Y":2,"Z":3}

Loss={"A":"Z","B":"X","C":"Y"}

Draw={"A":"X","B":"Y","C":"Z"}

def game_score(p1,p2):
    if p1 not in Loss.keys() or p2 not in Val.keys():
        raise ValueError
    res=Val[p2]
    if(Loss[p1]==p2):
        return res
    if(Draw[p1]==p2):
        return res+3
    return res+6



if __name__ == "__main__":
    f = open("input", "r")
    # f = open("test", "r")
    score=0
    for line in f:
        p=line.split()
        score+=game_score(p[0],p[1])
    
    print(score)
        