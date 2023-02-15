from copy import deepcopy
action = ["Up", "Right","Down","Left"]
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

class node: 
    def __init__(self, curent_position, action, cost, depth, parent, empty_tile_position, heuristic = 0 ) -> None:
        self.state = curent_position
        self.parent = parent
        self.action = action 
        self.cost = cost 
        self.depth = depth
        self.empty_tile = empty_tile_position
        self.heuristic = heuristic
    
    def __repr__(self):
        return f"current state: {self.state} \t parent: {self.parent} \t action:{self.action} \t cost:{self.cost} \t depth:{self.depth} \t empty_tile:{self.empty_tile}"
    
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

    def successor(self,state,parent):
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
                successor.append(node(temp,f"Move {cost} {action[i]}",state.cost+cost,state.depth+1,parent,new_tile_pos))
        return successor


    def heuristic(self):
    total_cost = 0
    for i in range(3):
        for j in range(3):
            if self.state[i][j] != 0:
                target_i, target_j = divmod(self.state[i][j]-1, 3)
                total_cost += abs(i - target_i) + abs(j - target_j)
                total_cost += self.state[i][j]  
    return total_cost