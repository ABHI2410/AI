import math

def red_blue_nim():
    # initialize the game with two piles of marbles
    red_pile = int(input("Enter the number of red marbles: "))
    blue_pile = int(input("Enter the number of blue marbles: "))
    player = 1  # human player goes first
    
    while True:
        if red_pile == 0 or blue_pile == 0:
            score = 2 * red_pile + 3 * blue_pile
            print("Game over. Player", player, "wins", score, "points.")
            break

        print("Red pile: ", red_pile, ", Blue pile: ", blue_pile)
        
        if player == 1:
            pile_choice = input("Which pile do you want to pick from? (r/b): ")
            if pile_choice == 'r':
                red_pile -= 1
            elif pile_choice == 'b':
                blue_pile -= 1
            else:
                print("Invalid input. Try again.")
                continue
        else:
            print("Computer is thinking...")
            # call the minimax algorithm to find the best move for the computer player
            pile_choice, _ = minimax(red_pile, blue_pile, 2, True, -math.inf, math.inf)
            if pile_choice == 'r':
                red_pile -= 1
            elif pile_choice == 'b':
                blue_pile -= 1
        
        player = 3 - player  # switch player

def evalfunction(is_maximizing,red_pile, blue_pile):
    marbles = red_pile + blue_pile
    score = 2 * red_pile + 3 * blue_pile
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
def minimax(red_pile, blue_pile, depth, is_maximizing, alpha, beta):
    if depth == 0:
        score = evalfunction(is_maximizing,red_pile, blue_pile)
        return None, score
    if red_pile == 0 or blue_pile == 0:
        score = 2 * red_pile + 3 * blue_pile
        return None, score
    
    if is_maximizing:
        best_score = -math.inf
        best_choice = None
            
        if blue_pile > 1:
            new_blue_pile = blue_pile - 1
            _, score = minimax(red_pile, new_blue_pile, depth - 1, False, alpha, beta)
            if score > best_score:
                best_score = score
                best_choice = 'b'
            alpha = max(alpha, score)
            if alpha >= beta:
                return best_choice, best_score
        
        elif red_pile > 1:
            new_red_pile = red_pile - 1
            _, score = minimax(new_red_pile, blue_pile, depth - 1, False, alpha, beta)
            if score > best_score:
                best_score = score
                best_choice = 'r'
            alpha = max(alpha, score)
            if alpha >= beta:
                return best_choice, best_score
        else:
            new_blue_pile = blue_pile - 1
            _, score = minimax(red_pile, new_blue_pile, depth - 1, False, alpha, beta)
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
            _, score = minimax(new_red_pile, blue_pile, depth - 1, True, alpha, beta)
            if score < best_score:
                best_score = score
                best_choice = 'r'
            beta = min(beta, score)
            if beta <= alpha:
                return best_choice, best_score
            
        elif blue_pile > 1:
            new_blue_pile = blue_pile - 1
            _, score = minimax(red_pile, new_blue_pile, depth - 1, True, alpha, beta)
            if score < best_score:
                best_score = score
                best_choice = 'b'
            alpha = min(alpha, score)
            if beta <= alpha:
                return best_choice, best_score
        else:
            new_red_pile = red_pile - 1
            _, score = minimax(new_red_pile, blue_pile, depth - 1, True, alpha, beta)
            if score < best_score:
                best_score = score
                best_choice = 'r'
            beta = min(beta, score)
            if beta <= alpha:
                return best_choice, best_score
                
        return best_choice, best_score
    
if __name__ == "__main__":
    red_blue_nim()