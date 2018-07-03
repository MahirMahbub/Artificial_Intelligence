import queue

class Graph(object):

    def __init__(self, r, n):
        self.current_state = (1, 1)
        self.prob_q = queue.Queue()
        self.no_prob_q = queue.Queue()
        self.r = r
        self.n = n
        self.probed = []

    def heuristic(self, r, x, y, n):
        return r - pow(x, n) - pow (y, n)

    def steppest_hill_climbing(self, state_x=1, state_y=1):

        self.current_state = (state_x, state_y)
        self.prob_q.put(self.current_state)
        self.probed.append(self.current_state)
        self.steppest_util(self.current_state[0], self.current_state[1])

    def steppest_util(self,state_x, state_y):
        print(self.current_state)
        if self.prob_q.empty():
            exit()
        self.current_state = self.prob_q.get()
        #print(self.current_state)
        heuristic_value = self.heuristic(self.r, self.current_state[0], self.current_state[1], self.n)
        if heuristic_value == 0:
            print("result",state_x-1, state_y)
            print( count )
            exit()
        elif heuristic_value > 0:
            left_heuristic = self.heuristic(self.r, self.current_state[0]+1, self.current_state[1], self.n)
            right_heuristic = self.heuristic(self.r, self.current_state[0], self.current_state[1]+1, self.n)
            #print(self.current_state)
            if left_heuristic> right_heuristic:
                #print(self.no_prob_q.qsize())
                self.no_prob_q.put((self.current_state[0]+1, self.current_state[1]))
                self.right_operation( heuristic_value, right_heuristic )
            else:
                #print( self.no_prob_q.qsize() )
                self.no_prob_q.put( (self.current_state[0], self.current_state[1]+1) )
                self.left_operation( heuristic_value, left_heuristic)
        else:
            if self.prob_q.empty():
                print("Iterate: "+str(count))
                return
        return

            #self.steppest_util(*self.current_state)


            # left_heuristic = self.heuristic( self.r, self.current_state[0] + 1, self.current_state[1], self.n )
            # right_heuristic = self.heuristic( self.r, self.current_state[0], self.current_state[1] + 1, self.n )
            # print( self.current_state )
            # if left_heuristic < right_heuristic:
            #     # print(self.no_prob_q.qsize())
            #     self.no_prob_q.put( (self.current_state[0] + 1, self.current_state[1]) )
            #     self.right_operation( heuristic_value, right_heuristic )
            # else:
            #     # print( self.no_prob_q.qsize() )
            #     self.no_prob_q.put( (self.current_state[0], self.current_state[1] + 1) )
            #     self.left_operation( heuristic_value, left_heuristic )


    def left_operation(self, heuristic_value, left_heuristic):
        if left_heuristic < heuristic_value and not (self.current_state[0] + 1, self.current_state[1]) in self.probed:
            self.prob_q.put( (self.current_state[0] + 1, self.current_state[1] ))
            self.probed.append( (self.current_state[0] + 1, self.current_state[1]) )
            self.current_state = (self.current_state[0] + 1, self.current_state[1])
        elif left_heuristic < heuristic_value and (self.current_state[0] + 1, self.current_state[1]) in self.probed:
            n_p = self.no_prob_q.get()
            self.prob_q.put( n_p )
            self.probed.append( n_p )
            self.current_state = n_p
            #print("here")
            #(state_x, state_y) = n_p
        elif left_heuristic >= heuristic_value:
            if not self.no_prob_q.empty():
                n_p = self.no_prob_q.get()
                self.prob_q.put( n_p )
                self.probed.append( n_p )
                self.current_state = n_p
        #self.no_prob_q.put( (state_x, state_y + 1) )
        #print( self.probed )
        self.steppest_util( self.current_state[0] + 1, self.current_state[1] )
        #self.steppest_util( state_x , state_y+1 )
        #print(self.current_state)

    def right_operation(self, heuristic_value, right_heuristic):
        if right_heuristic < heuristic_value and not (self.current_state[0],self.current_state[1] + 1) in self.probed:
            self.prob_q.put( (self.current_state[0], self.current_state[1] + 1 ))
            self.probed.append( (self.current_state[0], self.current_state[1] + 1) )
            self.current_state = (self.current_state[0], self.current_state[1]+1)
        elif right_heuristic < heuristic_value and (self.current_state[0], self.current_state[1] + 1) in self.probed:
            n_p = self.no_prob_q.get()
            self.prob_q.put( n_p )
            self.probed.append( n_p )
            self.current_state = n_p
            #print( "here" )
        elif right_heuristic >= heuristic_value:
            if not self.no_prob_q.empty():
                n_p = self.no_prob_q.get()
                self.prob_q.put( n_p )
                self.probed.append( n_p )
                self.current_state = n_p
        #self.no_prob_q.put(( state_x + 1, state_y ))
        #print(self.probed)
        self.steppest_util( self.current_state[0], self.current_state[1] + 1 )

        #self.steppest_util( state_x + 1, state_y )
        #print( self.current_state )


if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(1000000000)
    g = Graph(250 , 2)
    count = 0
    while(True):
        g.steppest_hill_climbing(1,1)
        count+=1
        if count == 10000:
            print("Iteration Limit exceed")
            break

