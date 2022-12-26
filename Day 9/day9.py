
#Use for better readability
x,y=('x','y')

class Rope:

    H={x:0, y:0}
    T={x:0, y:0}
    
    Tail_visits={(0,0)}

    directions={'R': 1, 'U': 1, 'L': -1, 'D': -1}
    coor={'R': x, 'U': y, 'L': x, 'D': y}

    def distance_H_T(self):
        return max( abs(self.diff_x()), abs(self.diff_y()) )

    def diff_x(self):
        return self.H[x]-self.T[x]
    
    def diff_y(self):
        return self.H[y]-self.T[y]
    
    def update_T(self) -> None:
        if(self.distance_H_T()<2 ):
            return None

        if(self.H[x]>self.T[x]):
            self.T[x]+=1
        elif(self.H[x]<self.T[x]):
            self.T[x]-=1
        
        if(self.H[y]>self.T[y]):
            self.T[y]+=1
        elif(self.H[y]<self.T[y]):
            self.T[y]-=1

        self.Tail_visits.add( (self.T[x],self.T[y]) )

    def move_H(self,direction,amount):
        for _ in range(amount):
            self.H[self.coor[direction]]+=self.directions[direction]
            self.update_T()
            # print( f' H:({rope.H[x]},{rope.H[y]}), T:({rope.T[x]},{rope.T[y]}) ')


if __name__ == "__main__":
    f = open("input", "r")
    # f = open("test", "r")
    result=0

    rope=Rope()

    for line in f:
        direction=line[0]
        n=int(line.split()[1])
        rope.move_H(direction,n)

    result=len(rope.Tail_visits)
    print(result)
