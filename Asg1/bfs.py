class bfs:
    def __init__(self, source, goal, dump_flag = False):
        start_state = source
        goal_state = goal
        dump = dump_flag
        node_popped = 0
        node_expanded = 0
        node_generated = 0
        max_fringe_size = 0 
        fringe = []
        closed = []
        state_archive = {}
    
    def generate_successor(self,node):
        successor = []
        self.node_generated += len(successor)
        return successor

    def graphSearch(self):
        start = self.create_state_strucutre(self.start_state,{"Start"},0,0,None)
        pos = len(self.state_archive)
        self.state_archive[pos] = start
        self.fringe.append(start)
        while len(self.fringe) is not 0:
            test_first_elem = self.fringe.pop(0)
            self.node_popped += 1
            if test_first_elem.get("position") == self.goal_state:
                return test_first_elem
            else:
                if test_first_elem.get("position") is not in self.closed:
                    self.closed.append(test_first_elem.get("position"))
                    self.fringe.append(self.generate_successor(test_first_elem))
                    self.node_expanded += 1
                    if self.max_fringe_size < len(self.fringe):
                        self.max_fringe_size = len(self.fringe)
            self.current_depth += 1
        if len(self.fringe) == 0:
            return False


