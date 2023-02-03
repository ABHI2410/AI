from dls import dls
from datastructure import Stack

class ids:
    def __init__(self, source, goal, file_name, dump_flag = False):
        self.start_state = source
        self.goal_state = goal
        self.file_name = file_name
        self.dump = dump_flag
        self.node_popped = 0
        self.node_expanded = 0
        self.node_generated = 0
        self.max_fringe_size = 0 
        self.fringe = Stack()
        self.closed = []
        self.state_archive = {}
        self.data_dump = ""

    def ids(self):
        i = 0
        while i>=-1:
            state = dls(self.start_state, self.goal_state,self.file_name,i,self.dump)
            result = state.graphSearch()
            if not result:
                print("Solution not found at depth ", i)
            else: 
                break
            i += 1

    