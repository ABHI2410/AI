from copy import deepcopy
action = ["Up", "Right","Down","Left"]
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

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
    
    def __repr__(self):
        return f"current state: {self.state} \t goal state: {self.goal} \t parent: {self.parent} \t action:{self.action} \t cost:{self.cost} \t depth:{self.depth} \t empty_tile:{self.empty_tile} \t heuristic = {self.heuristic}"
    
class Tools:

    def find_zero_position(self,state):
        count = 0
        for i in range(0,3):
            for j in range(0,3):
                count += 1
                if state[i][j] == 0:
                    return (i,j,count)

    def result(self,depth,cost,steps,node_popped,node_generated,node_expanded,max_fringe_size):
        out = f"""Nodes Popped: {node_popped} \nNodes Expanded: {node_expanded} \nNodes Generated: {node_generated} \nMax Fringe Size: {max_fringe_size}\nSolution Found at depth {depth} with cost of {cost}. \nSteps: \n"""
        steps.reverse()
        for item in steps:
            out += "     "+str(item) + "\n"
        return out

    def successor(self,state,parent,method=None):
        successor = []
        def isSafe(x,y):
            return x >= 0 and x < 3 and y >= 0 and y < 3
        for i in range(4):
            new_tile_pos = [state.empty_tile[0] + row[i],state.empty_tile[1] + col[i]]

            if isSafe(new_tile_pos[0],new_tile_pos[1]):
                temp = deepcopy(state.state)
                cost = state.state[new_tile_pos[0]][new_tile_pos[1]]
                temp[new_tile_pos[0]][new_tile_pos[1]] = 0
                temp[state.empty_tile[0]][state.empty_tile[1]] = cost 
                heuristc = 0
                if method == "greedy":
                    heuristc = self.heuristic(temp,state.goal)
                elif method == "a*" or method == "A*":
                    heuristc = self.heuristicwithcost(temp,state.goal) + state.cost
                else:
                    pass
                n1 = node(temp,state.goal,f"Move {cost} {action[i]}",state.cost+cost,state.depth+1,parent,new_tile_pos,heuristic=heuristc)
                successor.append(n1)
        return successor

    def heuristic(self,start,goal):
        goal_loc = {}
        board_loc = {}
        for i in range(0,3):
            for j in range (0,3):
                board_loc[start[i][j]] = (i,j)
                goal_loc[goal[i][j]] = (i,j)
        tcost = 0
        for i in range(0,9):
            cost = abs(board_loc.get(i)[0]-goal_loc.get(i)[0]) + abs(board_loc.get(i)[1]-goal_loc.get(i)[1])
            tcost += cost + i
        return(tcost)
    
    def heuristicwithcost(self,start,goal):
        goal_loc = {}
        board_loc = {}
        for i in range(0,3):
            for j in range (0,3):
                board_loc[start[i][j]] = (i,j)
                goal_loc[goal[i][j]] = (i,j)
        tcost = 0
        for i in range(0,9):
            cost = abs(board_loc.get(i)[0]-goal_loc.get(i)[0]) + abs(board_loc.get(i)[1]-goal_loc.get(i)[1])
            tcost += cost * i
        return(tcost)
