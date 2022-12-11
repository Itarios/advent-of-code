# A for Rock, B for Paper, and C for Scissors
# X for Lose Y for Draw, and Z for Win

def shift_list(l):
    l.append(l.pop(0))

Val1={"A":1, "B":2,"C":3}

Val2={"X":0, "Y":1,"Z":2}

Draw={"A":"A","B":"B","C":"C"}
Win={"A":"B","B":"C","C":"A"}
Loss={"A":"C","B":"A","C":"B"}

Player2=[Loss,Draw,Win]

def game_score(v1,v2):
    if v1 not in Val1.keys() or v2 not in Val2.keys():
        raise ValueError

    #Player2 gives the shape for player 2 given by strategy and the player 1
    
    return Val1[ Player2[Val2[v2]][v1] ] + Val2[v2]*3


if __name__ == "__main__":
    f = open("input", "r")
    # f = open("test", "r")
    score=0
    for line in f:
        p=line.split()
        score+=game_score(p[0],p[1])
    
    print(score)
        