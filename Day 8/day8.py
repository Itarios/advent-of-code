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
    # forest.pop()
      
    
    result=visible_trees(forest)

    print(result)
