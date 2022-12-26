
#Use for better readability
x,y=('x','y')

class Rope:

    def __init__(self, n) -> None:
        self.H={x:0, y:0}
        self.Knots=[self.H]
        self.n=n+1
        for _ in range(n):
            self.Knots.append( dict(self.H) )
        
        self.T=self.Knots[n]

        self.Tail_visits={ self.knot_to_coordinate(n) }

    directions={'R': 1, 'U': 1, 'L': -1, 'D': -1}
    coor={'R': x, 'U': y, 'L': x, 'D': y}

    def knot_to_coordinate(self,knot):
        return (self.Knots[knot][x], self.Knots[knot][y])
        

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

    
    def abs_diff_x_knot(self,knot):
        return abs(self.Knots[knot][x]-self.Knots[knot-1][x])

    def abs_diff_y_knot(self,knot):
        return abs(self.Knots[knot][y]-self.Knots[knot-1][y])
    
    def distance_consecutive_knots(self,knot):
        return max( self.abs_diff_x_knot(knot),self.abs_diff_y_knot(knot)  )

    def update_knots(self):
        for knot in range(1,self.n):
            
            if( self.distance_consecutive_knots(knot)<2 ):
                continue

            if(self.Knots[knot-1][x]>self.Knots[knot][x]):
                self.Knots[knot][x]+=1
            elif(self.Knots[knot-1][x]<self.Knots[knot][x]):
                self.Knots[knot][x]-=1
            
            if(self.Knots[knot-1][y]>self.Knots[knot][y]):
                self.Knots[knot][y]+=1
            elif(self.Knots[knot-1][y]<self.Knots[knot][y]):
                self.Knots[knot][y]-=1

            self.Tail_visits.add( self.knot_to_coordinate(self.n-1) )

    def move_H(self,direction,amount):
        # print(self.H, direction, amount)
        for _ in range(amount):
            self.H[self.coor[direction]]+=self.directions[direction]
            # self.update_T()
            self.update_knots()
        



if __name__ == "__main__":
    f = open("input", "r")
    # f = open("test", "r")
    # f = open("test2", "r")
    result=0

    rope=Rope(9)

    for line in f:
        direction=line[0]
        n=int(line.split()[1])
        rope.move_H(direction,n)

    result=len(rope.Tail_visits)
    print(result)
