class Tools:
    def create_state_strucutre(self, curent_position, action, cost, depth, parent ):
        state = {"position": curent_position, "action": action, "g(n)": cost, "depth" : depth, "parent": parent}
        return state

    def find_zero_position(self,state):
        count = 0
        for i in range(0,3):
            for j in range(0,3):
                count += 1
                if state[i][j] == 0:
                    return (i,j,count)

    def get_legal_moves(self,state):
        successor = []
        row, col, pos = self.find_zero_position(state.get("position"))
        possible_successor = [2,3,2,3,4,3,2,3,2,]
        number_of_successor = possible_successor[pos]
        if number_of_successor == 4:
            new_state = state.get("position")
            new_state[0][1],new_state[1],[1] = new_state[1],[1], new_state[0][1]
            parent = [key for key, val in self.state_archive if val == state]
            temp_successor = self.create_state_strucutre(new_state, f"Move {new_state[1][1]} Down", new_state[1][1], state.get("depth")+1, parent[0])
            pos = len(self.state_archive)
            self.state_archive[pos] = temp_successor
            successor.append(temp_successor)


            new_state = state.get("position")
            new_state[1][0],new_state[1],[1] = new_state[1],[1], new_state[1][0]
            parent = [key for key, val in self.state_archive if val == state]
            temp_successor = self.create_state_strucutre(new_state, f"Move {new_state[1][1]} Left", new_state[1][1], state.get("depth")+1, parent[0])
            pos = len(self.state_archive)
            self.state_archive[pos] = temp_successor
            successor.append(temp_successor)

            new_state = state.get("position")
            new_state[1][2],new_state[1],[1] = new_state[1],[1], new_state[1][2]
            parent = [key for key, val in self.state_archive if val == state]
            temp_successor = self.create_state_strucutre(new_state, f"Move {new_state[1][1]} Right", new_state[1][1], state.get("depth")+1, parent[0])
            pos = len(self.state_archive)
            self.state_archive[pos] = temp_successor
            successor.append(temp_successor)

            new_state = state.get("position")
            new_state[2][1],new_state[1],[1] = new_state[1],[1], new_state[2][1]
            parent = [key for key, val in self.state_archive if val == state]
            temp_successor = self.create_state_strucutre(new_state, f"Move {new_state[1][1]} Up", new_state[1][1], state.get("depth")+1, parent[0])
            pos = len(self.state_archive)
            self.state_archive[pos] = temp_successor
            successor.append(temp_successor)

        elif number_of_successor == 2:
            if row == 0 and col == 0:
                new_state =state.get("position")
                new_state[0][0], new_state [0][1] = new_state[0][1], new_state[0][0]
                parent = [key for key, val in self.state_archive if val == state]
                temp_successor = self.create_state_strucutre(new_state, f"Move {new_state[0][1]} Left", new_state[0][1], state.get("depth")+1, parent[0])
                pos = len(self.state_archive)
                self.state_archive[pos] = temp_successor
                successor.append(temp_successor)

                new_state =state.get("position")
                new_state[0][0], new_state [1][0] = new_state[1][0], new_state[0][0]
                parent = [key for key, val in self.state_archive if val == state]
                temp_successor = self.create_state_strucutre(new_state, f"Move {new_state[1][0]} Up", new_state[1][0], state.get("depth")+1, parent[0])
                pos = len(self.state_archive)
                self.state_archive[pos] = temp_successor
                successor.append(temp_successor)

            elif row == 0 and col == 2:

        elif number_of_successor == 3:
            
        else:
            return False
        return successor
