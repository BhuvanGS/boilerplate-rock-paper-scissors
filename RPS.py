# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    # First move (no previous play)
    if prev_play == '':
        opponent_history.clear()
        return 'R'  # Start with Rock
    
    # Add the opponent's previous move to history
    opponent_history.append(prev_play)
    
    # If we have very few moves, use a simple strategy
    if len(opponent_history) < 10:
        # Counter the previous move
        if prev_play == 'R':
            return 'P'  # Paper beats Rock
        elif prev_play == 'P':
            return 'S'  # Scissors beats Paper
        else:
            return 'R'  # Rock beats Scissors
    
    # Start looking for patterns in the last moves
    last_moves = ''.join(opponent_history[-5:])
    
    # Check for pattern in opponent's last 4 moves to predict the 5th
    patterns = {}
    for i in range(len(opponent_history) - 4):
        pattern = ''.join(opponent_history[i:i+4])
        next_move = opponent_history[i+4]
        
        if pattern in patterns:
            patterns[pattern][next_move] = patterns[pattern].get(next_move, 0) + 1
        else:
            patterns[pattern] = {next_move: 1}
    
    # Get the most recent 4 moves
    current_pattern = ''.join(opponent_history[-4:])
    
    # Predicted move based on pattern
    predicted_move = None
    if current_pattern in patterns:
        # Find the most likely next move based on pattern history
        max_count = 0
        for move, count in patterns[current_pattern].items():
            if count > max_count:
                max_count = count
                predicted_move = move
    
    # If we found a pattern, counter the predicted move
    if predicted_move:
        if predicted_move == 'R':
            return 'P'
        elif predicted_move == 'P':
            return 'S'
        else:  # 'S'
            return 'R'
    
    # If no clear pattern, check for frequency bias in recent moves
    recent_moves = opponent_history[-10:]
    rock_count = recent_moves.count('R')
    paper_count = recent_moves.count('P')
    scissors_count = recent_moves.count('S')
    
    if rock_count > paper_count and rock_count > scissors_count:
        return 'P'  # They play Rock most, counter with Paper
    elif paper_count > rock_count and paper_count > scissors_count:
        return 'S'  # They play Paper most, counter with Scissors
    elif scissors_count > rock_count and scissors_count > paper_count:
        return 'R'  # They play Scissors most, counter with Rock
    
    # If all else fails, counter the last move
    if prev_play == 'R':
        return 'P'
    elif prev_play == 'P':
        return 'S'
    else:
        return 'R'