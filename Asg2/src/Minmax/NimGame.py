import math


## Class for Nim game.
class NimGame:

    ## Initializing all class varialbles
    def __init__(self,red,blue,depth,first_player) -> None:
        self.red_marbles = red
        self.blue_marbles = blue
        self.depth = depth
        self.player = first_player
        self.score = 0
        self.players = {1:"Human", 2: "Computer"}
        self.color = {'r': "Red", 'b':"Blue"}

    ## Evaluation function to find mimmax value
    def eval_function(self,is_maximizing,red_marbles, blue_marbles):
        marbles = red_marbles + blue_marbles
        score = 2 * red_marbles + 3 * blue_marbles
        if is_maximizing:
            if marbles%2 == 0:
                return -score
            else:
                return score
        else:
            if marbles%2 == 0:
                return score
            else:
                return -score
    ## Main game playing function 
    def nimgame(self):
        # infinit loop till the game ends
        while True:
            if self.red_marbles == 0 or self.blue_marbles == 0:
                self.score = 2 * self.red_marbles + 3 * self.blue_marbles
                print(f"Game over.\n{self.players.get(self.player)} wins by {self.score} points.")
                break
            
            ## printing current state of the game
            print(f"Red marbles:{self.red_marbles} Blue marbles:{self.blue_marbles}")
            
            ## Human player turn 
            if self.player == 1:
                marble_choice = input("Which marble do you want to pick from? (r/b): ")
                if marble_choice == 'r' or marble_choice == 'R':
                    self.red_marbles -= 1
                elif marble_choice == 'b' or marble_choice == 'B':
                    self.blue_marbles -= 1
                else:
                    print("Invalid input. Try again.")
                    continue

            ## Computer turn
            else:
                print("Computer is thinking...")
                # call the minimax algorithm to find the best move for the computer player
                marble_choice, _ = self.minimax(self.red_marbles, self.blue_marbles, self.depth, True, -math.inf, math.inf)
                print(f"Computer picks {self.color.get(marble_choice)}")
                if marble_choice == 'r':
                    self.red_marbles -= 1
                elif marble_choice == 'b':
                    self.blue_marbles -= 1
            #switch player 
            self.player = 3 - self.player

    ## MinMax Algorithm 
    def minimax(self,red_pile, blue_pile, depth, is_maximizing, alpha, beta):
        if depth == 0:
            score = self.eval_function(is_maximizing,red_pile, blue_pile)
            return None, score
        if red_pile == 0 or blue_pile == 0:
            score = 2 * red_pile + 3 * blue_pile
            return None, score
        
        if is_maximizing:
            best_score = -math.inf
            best_choice = None
                
            if blue_pile > 1:
                new_blue_pile = blue_pile - 1
                _, score = self.minimax(red_pile, new_blue_pile, depth - 1, False, alpha, beta)
                if score > best_score:
                    best_score = score
                    best_choice = 'b'
                alpha = max(alpha, score)
                if alpha >= beta:
                    return best_choice, best_score
            
            if red_pile > 1:
                new_red_pile = red_pile - 1
                _, score = self.minimax(new_red_pile, blue_pile, depth - 1, False, alpha, beta)
                if score > best_score:
                    best_score = score
                    best_choice = 'r'
                alpha = max(alpha, score)
                if alpha >= beta:
                    return best_choice, best_score
            if red_pile == 1 and blue_pile == 1:
                new_blue_pile = blue_pile - 1
                _, score = self.minimax(red_pile, new_blue_pile, depth - 1, False, alpha, beta)
                if score > best_score:
                    best_score = score
                    best_choice = 'b'
                alpha = max(alpha, score)
                if alpha >= beta:
                    return best_choice, best_score
                    
            return best_choice, best_score
        
        else:
            best_score = math.inf
            best_choice = None
            
            if red_pile > 1:
                new_red_pile = red_pile - 1
                _, score = self.minimax(new_red_pile, blue_pile, depth - 1, True, alpha, beta)
                if score < best_score:
                    best_score = score
                    best_choice = 'r'
                beta = min(beta, score)
                if beta <= alpha:
                    return best_choice, best_score
                
            if blue_pile > 1:
                new_blue_pile = blue_pile - 1
                _, score = self.minimax(red_pile, new_blue_pile, depth - 1, True, alpha, beta)
                if score < best_score:
                    best_score = score
                    best_choice = 'b'
                alpha = min(alpha, score)
                if beta <= alpha:
                    return best_choice, best_score
            if red_pile == 1 and blue_pile == 1:
                new_blue_pile = blue_pile - 1
                _, score = self.minimax(red_pile, new_blue_pile, depth - 1, True, alpha, beta)
                if score < best_score:
                    best_score = score
                    best_choice = 'b'
                alpha = min(alpha, score)
                if beta <= alpha:
                    return best_choice, best_score
                    
            return best_choice, best_score
        
