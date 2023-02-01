from tools import node,Tools
class dfs:
    def __init__(self, source, goal, file_name, dump_flag = False):
        self.start_state = source
        self.goal_state = goal
        self.file_name = file_name
        self.dump = dump_flag
        self.node_popped = 0
        self.node_expanded = 0
        self.node_generated = 0
        self.max_fringe_size = 0 
        self.fringe = []
        self.closed = []
        self.state_archive = {}
        self.data_dump = ""
    
    def result(self,depth,cost,steps):
        out = f"""Nodes Popped: {self.node_popped} \nNodes Expanded: {self.node_expanded} \nNodes Generated: {self.node_generated} \nMax Fringe Size: {self.max_fringe_size}\nSolution Found at depth {depth} with cost of {cost}. \nSteps: \n"""
        steps.reverse()
         
        for item in steps:
            out += "     "+str(item) + "\n"
        return out
    
    def generate_successor(self,node,pos):
        successor = Tools().successor(node,pos)
        self.node_generated += len(successor)
        return successor

    def graphSearch(self):
        if self.dump:
            with open (self.file_name,'a+') as text_file:
                text_file.write(f"Start State: {self.start_state} \nGoal State: {self.goal_state} \nFringe: {self.fringe}\nClosed list: {self.closed}.\nStarting Graph Search in BFS Fashion\n")
                text_file.close()
        empty_tile = Tools().find_zero_position(self.start_state)
        start = node(self.start_state,{"Start"},0,0,None,empty_tile)
        self.fringe.append(start)
        if self.dump:
            with open (self.file_name,'a+') as text_file:
                text_file.write(f"Adding Start State to fringe.\nCurrent Fringe: {self.fringe}\n\n")
                text_file.close()
        steps = []
        while len(self.fringe) != 0:
            pos = len(self.state_archive)
            test_first_elem = self.fringe.pop(-1)
            if self.dump:
                with open (self.file_name,'a+') as text_file:
                    text_file.write(f"Popping 1st element from fringe.\n")
                    text_file.close()
            self.state_archive[pos] = test_first_elem
            self.node_popped += 1
            if test_first_elem.state == self.goal_state:
                if self.dump:
                    with open (self.file_name,'a+') as text_file:
                        text_file.write(f"Current State is the Goal State.\n Search Successfull!!! \n")
                        text_file.close()
                depth = test_first_elem.depth
                cost = test_first_elem.cost
                while test_first_elem.parent != None:
                    steps.append(test_first_elem.action)
                    test_first_elem = self.state_archive.get(test_first_elem.parent)
                result = self.result(depth,cost,steps)
                print(result)
                if self.dump:
                    with open (self.file_name,'a+') as text_file:
                        text_file.write(f"{result}\n")
                        text_file.close()
                break
            else:
                if self.dump:
                    with open (self.file_name,'a+') as text_file:
                        text_file.write(f"Current state is not goal state, generating successors.\nGenerating successors to state > {test_first_elem}\n")
                        text_file.close()
                if test_first_elem.state not in self.closed:
                    self.closed.append(test_first_elem.state)
                    suc = self.generate_successor(test_first_elem,pos)
                    if self.dump:
                        with open (self.file_name,'a+') as text_file:
                            text_file.write(f"{len(suc)} successors generated.\nAdding current state to closed list.\nClosed list: {self.closed}.\n")
                            text_file.close()
                    for item in suc:
                        self.fringe.append(item)
                    if self.dump:
                        with open (self.file_name,'a+') as text_file:
                            text_file.write(f"Fringe: {self.fringe}\n\n")
                            text_file.close()
                    self.node_expanded += 1
                    if self.max_fringe_size < len(self.fringe):
                        self.max_fringe_size = len(self.fringe)            


