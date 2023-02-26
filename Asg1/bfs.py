#Required imports
from tools import node,Tools
from datastructure import Queue

## Main class to implement a* algorithm using graph search.
class bfs:
    ## initialization function assigning class vairables to the inputs recived as arrugments to the class. 
    def __init__(self, source, goal, file_name, dump_flag = False):
        self.start_state = source
        self.goal_state = goal
        self.file_name = file_name
        self.dump = dump_flag
        self.node_popped = 0
        self.node_expanded = 0
        self.node_generated = 0
        self.max_fringe_size = 0 
        self.fringe = Queue() ## Initializing fringe as queue which is imported form datastrucute module.
        self.closed = [] ## initializing closed set.
        self.state_archive = {} ## initializing a dict to keep track of the states that are already generated so they can be represented by a number instead of a nested node.
        self.data_dump = ""
    
    ## Successor generator function. 
    def generate_successor(self,node,pos):
        successor = Tools().successor(node,pos) ## gives a function call to successor function in Tools class from tools module.
        self.node_generated += len(successor) ## Updating the count of nodes generated
        return successor ## returns list of successors 

    ## Main graph search function 
    def graphSearch(self):

        ## log file entry 
        if self.dump:
            with open (self.file_name,'a+') as text_file:
                text_file.write(f"Start State: {self.start_state} \nGoal State: {self.goal_state} \nFringe: {self.fringe}\nClosed list: {self.closed}.\nStarting Graph Search in BFS Fashion\n")
                text_file.close()
        ## log file entry complete.

        empty_tile = Tools().find_zero_position(self.start_state) ## identifies the location of 0/empty tile in 8 puzzle problem.
        start = node(self.start_state,self.goal_state,{"Start"},0,0,None,empty_tile) ## creates the node in the required structure as defined in node class in tools.py
        self.fringe.enqueue(start) ## adding element to the fringe

        ## log file entry 
        if self.dump:
            with open (self.file_name,'a+') as text_file:
                text_file.write(f"Adding Start State to fringe.\nCurrent Fringe: {self.fringe}\n\n")
                text_file.close()
        ## log file entry complete.

        steps = [] ## initializing a list to keep track of steps taken to reach the solution.

        ## createing an loop that will run untill the fringe is empty.
        while not self.fringe.is_empty():
            pos = len(self.state_archive) ## identifying last available location in archive list.
            test_first_elem = self.fringe.dequeue() ## poping 1st element from the fringe.

            ## log file entry 
            if self.dump:
                with open (self.file_name,'a+') as text_file:
                    text_file.write(f"Popping 1st element from fringe.\n")
                    text_file.close()
            ## log file entry complete.

            self.state_archive[pos] = test_first_elem ## adding state to the archive list.
            self.node_popped += 1  ## updating count of node popped.

            if test_first_elem.state == self.goal_state: ## checking if the current state is the goal state or not.

                ## log file entry 
                if self.dump:
                    with open (self.file_name,'a+') as text_file:
                        text_file.write(f"Current State is the Goal State.\n Search Successfull!!! \n")
                        text_file.close()
                ## log file entry complete.

                depth = test_first_elem.depth ## identifying the current depth reached by search.
                cost = test_first_elem.cost  ## identifying the current cost incured to reach the state.
                
                ## loop to find the path taken to reach from start state to goal state.
                while test_first_elem.parent != None:
                    steps.append(test_first_elem.action) ## appeding actions taken to reach.
                    test_first_elem = self.state_archive.get(test_first_elem.parent) ## getting information of the parent of the current node.
                result = Tools().result(depth,cost,steps,self.node_popped,self.node_generated,self.node_expanded,self.max_fringe_size) ## creating result string as required.
                print(result)

                ## log file entry 
                if self.dump:
                    with open (self.file_name,'a+') as text_file:
                        text_file.write(f"{result}\n")
                        text_file.close()
                ## log file entry complete.

                return True ## end the loop and return to the main driver program in expense_8_puzzle.py
            
            ## Actions to perform if goal state is not found.
            else:

                ## log file entry 
                if self.dump:
                    with open (self.file_name,'a+') as text_file:
                        text_file.write(f"Current state is not goal state, generating successors.\nGenerating successors to state > {test_first_elem}\n")
                        text_file.close()
                ## log file entry complete.

                if test_first_elem.state not in self.closed: ## check if the current state is in the closed set.
                    self.closed.append(test_first_elem.state) ## if not add to the closed set
                    suc = self.generate_successor(test_first_elem,pos) ## generate successors for the current state.

                    ## log file entry 
                    if self.dump:
                        with open (self.file_name,'a+') as text_file:
                            text_file.write(f"{len(suc)} successors generated.\nAdding current state to closed list.\nClosed list: {self.closed}.\n")
                            text_file.close()
                    ## log file entry complete.

                    ## adding successors to the fringe
                    for item in suc:
                        self.fringe.enqueue(item)

                    ## log file entry 
                    if self.dump:
                        with open (self.file_name,'a+') as text_file:
                            text_file.write(f"Fringe: {self.fringe}\n\n")
                            text_file.close()
                    ## log file entry complete.

                    self.node_expanded += 1  ## updateing the count of nodes expanded
                    if self.max_fringe_size < self.fringe.len_queue(): ## checking for fringe size
                        self.max_fringe_size = self.fringe.len_queue()  ## update max fringe size if required.
        
        ## if fringe get empty and goal sate is not reached means solution does not exists.
        print("Solution not found")

        ## log file entry 
        if self.dump:
            with open (self.file_name,'a+') as text_file:
                text_file.write(f"Soultion no found\n")
                text_file.close()
        ## log file entry complete.

        return False ## return to the main function in expense_8_puzzle.py