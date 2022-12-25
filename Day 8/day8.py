

def count_geq(num,values):
    geq=[v for v in values if (v>=num)]
    return len( geq )

def visible_trees(forest):
    n=len(forest)
    m=len(forest[0])

    visible=2*(m+n)-4
    

    for i in range(1,n-1):
        
        for j in range(1,m-1):
            # up=[row[j] for row in forest[:i]]
            if(count_geq(forest[i][j], [row[j] for row in forest[:i] ] )==0):
                visible+=1
                continue

            # down=[row[j] for row in forest[i+1:]]
            if(count_geq(forest[i][j], [row[j] for row in forest[i+1:] ] )==0):
                visible+=1
                continue

            # left=forest[i][:j]
            if(count_geq(forest[i][j], forest[i][:j] )==0):
                visible+=1
                continue

            # right=forest[i][j+1:]
            if(count_geq(forest[i][j], forest[i][j+1:] )==0):
                visible+=1
                continue

    return visible


def scenic_score_direction(tree,direction):
    n=len(direction)

    for i in range(n):
        if(direction[i]>=tree):
            return i+1
    return n
    
def scenic_score(tree, up, down, left, right):
    score=scenic_score_direction(tree, up)
    score*=scenic_score_direction(tree, down)
    score*=scenic_score_direction(tree, left)
    score*=scenic_score_direction(tree, right)
    
    # print(tree,up,down,left,right, score)
    
    return score

def max_scenic_score(forest):
    n=len(forest)
    m=len(forest[0])

    max_ss=1
    

    for i in range(1,n-1):
        for j in range(1,m-1):
            down=[row[j] for row in forest[i+1:]]
            
            right=forest[i][j+1:]

            up= [row[j] for row in forest[:i]]

            left=forest[i][:j]

            up.reverse()
            left.reverse()

            max_ss= max( max_ss, scenic_score(forest[i][j],up,down,left,right) )

    return max_ss



if __name__ == "__main__":
    f = open("input", "r")
    # f = open("test", "r")
    result=0

    forest=[]

    for line in f:
        forest.append(list(line)[:-1])
    f.close()
    
    # print(forest)
    # print( len(forest) )
    # print( len(forest[0]) )
      
    
    # result=visible_trees(forest)

    result=max_scenic_score(forest)

    print(result)
