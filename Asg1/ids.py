#Required imports
from dls import dls
from datastructure import Stack

## Main class to implement a* algorithm using graph search.
class ids:
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
        self.fringe = Stack() ## Initializing fringe as Stack  which is imported form datastrucute module.
        self.closed = [] ## initializing closed set.
        self.state_archive = {} ## initializing a dict to keep track of the states that are already generated so they can be represented by a number instead of a nested node.
        self.data_dump = ""

    ## Main ids function 
    def ids(self):
        i = 0  ## initializing depth as 0

        ## creating an infite loop to increment depth till you find a solution
        while i>=-1:
            state = dls(self.start_state, self.goal_state,self.file_name,i,self.dump) ## using dls to find the soultion.
            result = state.graphSearch() ## fetching result of graph serch
            if not result:
                print("at depth: ",i)
            else: 
                return True
            i += 1
        
        print("Solution not found")

        ## log file entry
        if self.dump:
            with open (self.file_name,'a+') as text_file:
                        text_file.write(f"Soultion no found\n")
                        text_file.close()
        ## log file entry complete
        return False

    