

def count_less_than(num,values):
    return len( [v for v in values if (v<num)] )

def visible_trees(forest):
    n=len(forest)
    visible=4*(n-1)

    for i in range(1,n-1):
        for j in range( 1,n-1 ):
            # up=[row[j] for row in forest[:i]]
            if(count_less_than(forest[i][j], [row[j] for row in forest[:i]] )>0):
                visible+=1
                continue

            # down=[row[j] for row in forest[i+1:]]
            if(count_less_than(forest[i][j], [row[j] for row in forest[i+1:]] )>0):
                visible+=1
                continue

            # left=forest[i][:j]
            if(count_less_than(forest[i][j], forest[i][:j] )>0):
                visible+=1
                continue

            # right=forest[i][j+1:]
            if(count_less_than(forest[i][j], forest[i][j+1:] )>0):
                visible+=1
                continue

    return visible


if __name__ == "__main__":
    # f = open("input", "r")
    f = open("test", "r")
    result=0

    forest=[]

    for line in f:
        forest.append(list(line))
    f.close()   

    result=visible_trees(forest)

    print(result)
