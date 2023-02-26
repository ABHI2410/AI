## required imports
from copy import deepcopy

## gobals lists requied for actions and successor generation.
action = ["Up", "Right","Down","Left"]
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

## node class to create a node in the required formate
class node: 
    def __init__(self, curent_position, goal, action, cost, depth, parent, empty_tile_position, heuristic = 0 ) -> None:
        self.state = curent_position
        self.goal = goal
        self.parent = parent
        self.action = action 
        self.cost = cost 
        self.depth = depth
        self.empty_tile = empty_tile_position
        self.heuristic = heuristic
    
    ## representation funtion if node is required to be printed.
    def __repr__(self):
        return f"current state: {self.state} \t goal state: {self.goal} \t parent: {self.parent} \t action:{self.action} \t cost:{self.cost} \t depth:{self.depth} \t empty_tile:{self.empty_tile} \t heuristic = {self.heuristic}"

## Tools function that contains various diffent functions which may or may not be required
class Tools:

    ## function to locate the empty title or 0
    def find_zero_position(self,state):
        count = 0   
        ## loop through the board till you find the empty tile
        for i in range(0,3):
            for j in range(0,3):
                count += 1
                if state[i][j] == 0:
                    return (i,j,count)

    ## result representation funtion 
    def result(self,depth,cost,steps,node_popped,node_generated,node_expanded,max_fringe_size):
        out = f"""Nodes Popped: {node_popped} \nNodes Expanded: {node_expanded} \nNodes Generated: {node_generated} \nMax Fringe Size: {max_fringe_size}\nSolution Found at depth {depth} with cost of {cost}. \nSteps: \n"""
        steps.reverse()
        for item in steps:
            out += "     "+str(item) + "\n"
        return out

    ## successor generator function 
    def successor(self,state,parent,method=None):
        successor = []

        ## check if the postion can exist on the board or not
        def isSafe(x,y):
            return x >= 0 and x < 3 and y >= 0 and y < 3
        
        ## at max 4 successors can be generated top, bottom, left, right for running the loop for 4 times at each loaction 
        for i in range(4):
            ## generating the possible location to switch with empty tile to get successors
            new_tile_pos = [state.empty_tile[0] + row[i],state.empty_tile[1] + col[i]]
            
            ## if the new location can exsits on the board generate sucessor
            if isSafe(new_tile_pos[0],new_tile_pos[1]):
                temp = deepcopy(state.state)  ## create a copy of the current state 
                cost = state.state[new_tile_pos[0]][new_tile_pos[1]] ## use the tile face number as the cost
                temp[new_tile_pos[0]][new_tile_pos[1]] = 0 ## assign the new location to empty tile
                temp[state.empty_tile[0]][state.empty_tile[1]] = cost  ## assign the face value of the tile to switch with empty tile.
                heuristc = 0  ## set heuristc to 0 by default 

                ## if the method is greedy or a * generate heuristic values 
                if method == "greedy":
                    heuristc = self.heuristic(temp,state.goal)
                elif method == "a*" or method == "A*":
                    heuristc = self.heuristicwithcost(temp,state.goal) + state.cost
                else:
                    pass
                ## create the node with the new values 
                n1 = node(temp,state.goal,f"Move {cost} {action[i]}",state.cost+cost,state.depth+1,parent,new_tile_pos,heuristic=heuristc)
                successor.append(n1)  ## add the node to the successor list 
        return successor ## return successor list

    ## function to calculate heuristic 
    def heuristic(self,start,goal):
        goal_loc = {}
        board_loc = {}

        ## identify location of each number on both the current board and goal board
        for i in range(0,3):
            for j in range (0,3):
                board_loc[start[i][j]] = (i,j)
                goal_loc[goal[i][j]] = (i,j)
        tcost = 0

        ## calculate manhatan distace 
        for i in range(0,9):
            cost = abs(board_loc.get(i)[0]-goal_loc.get(i)[0]) + abs(board_loc.get(i)[1]-goal_loc.get(i)[1])
            tcost += cost + i
        
        return(tcost) ## return the heuristc value 
    

    ## function to calculate heuristic with cost of movement
    def heuristicwithcost(self,start,goal):
        goal_loc = {}
        board_loc = {}

        ## identify location of each number on both the current board and goal board
        for i in range(0,3):
            for j in range (0,3):
                board_loc[start[i][j]] = (i,j)
                goal_loc[goal[i][j]] = (i,j)
        tcost = 0
        ## calculate manhatan distace 
        for i in range(0,9):
            cost = abs(board_loc.get(i)[0]-goal_loc.get(i)[0]) + abs(board_loc.get(i)[1]-goal_loc.get(i)[1])
            tcost += cost * i

        return(tcost) ## return the heuristc value 
