###
# Lab 3 - 8-puzzle problem
###
import copy

# Function to generate the next state given a current state and an action
# - Copy the current state value into a new variable
# - Determine the location of the empty tile (this is the tile that will move)
# - Dbtain the information pertaining to the action
# - Perform the action - obtaining the new location that should contain the empty tile
# - If the action results in a valid state, then copy the tile in the new location
# (according to the current state) to the old location of the empty tile and
# assign 0 to the new location
def generate_next_state(current_state, action):
    next_state = copy.deepcopy(current_state)
    empty_row, empty_col = find_empty_tile(next_state)
    move_row, move_col = action
    next_row, next_col = empty_row + move_row, empty_col + move_col

    # Check if the move is valid (within bounds of the puzzle)
    if 0 <= next_row < len(current_state) and 0 <= next_col < len(current_state[0]):
        next_state[empty_row][empty_col] = next_state[next_row][next_col]
        next_state[next_row][next_col] = 0
        return next_state
    else:
        return None  # Invalid move, return None

# Function to find the empty tile in the puzzle
def find_empty_tile(state):
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 0:
                return row, col

# Function to check if the generated state is goal
def is_goal_state(state, goal_state):
    return state == goal_state

# Function to print the puzzle state in a visually appealing format
def print_puzzle(state):
    for row in state:
        print(' '.join(map(str, row)))
    print()

# Depth-First Search algorithm
# If the goal state is achievable, the function
# should return the sequence of states from the start state to the goal state
# Use a list (or another data structure) to store the states
# that have already been visited. This will require additional memory, 
# but will save us computational time.
def depth_first_search(start_state, goal_state):
    

# Breadth-First Search algorithm
# If the goal state is achievable, the function
# should return the sequence of states from the start state to the goal state
# Use a list (or another data structure) to store the states
# that have already been visited. This will require additional memory, 
# but will save us computational time.
def breadth_first_search(start_state, goal_state):
   

# Example usage
start_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

print("Depth-First Search:")
solution_dfs = depth_first_search(start_state, goal_state)
if solution_dfs:
    for step in solution_dfs:
        state, action = step
        print_puzzle(state)
        print("Action:", action)
else:
    print("No solution found.")

print("Breadth-First Search:")
solution_bfs = breadth_first_search(start_state, goal_state)
if solution_bfs:
    for step in solution_bfs:
        state, action = step
        print_puzzle(state)
        print("Action:", action)
else:
    print("No solution found.")
