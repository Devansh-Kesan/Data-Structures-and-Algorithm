###
# Lab 3 - 8-puzzle problem
###
import copy

class TreeNode:
    def __init__(self,val,move=(0,0)):
        self.val=val
        self.children=[]
        self.parent=None
        self.move=move
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        if self.parent==None:
            return 0
        return 1+self.parent.get_level()
    
    def is_leaf(self):
        if not self.children:
            return True
        return False
    
    def is_root(self):
        if not self.parent:
            return True
        return False

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

actions=[[0,-1],[0,1],[-1,0],[1,0]]

def breadth_first_search(start_state, goal_state):
    visited=[]
    visited.append([start_state,[]])
    queue=[]
    queue.append([start_state,[]])
    start,action=queue.pop(0)
    while start != goal_state:
        for i in actions:
            temp = generate_next_state(start,i)
            if temp:
                if temp not in visited:
                    visited.append([temp,i])
                    queue.append([temp,i])
        start,action=queue.pop(0)
    
    solutions_list=[(start,"Solution found")]
    start1=start
    action1=action
    while start1!=start_state:
        next_st=generate_next_state(start1,[-x for x in action1])
        for k in visited:
            if k[0] == next_st:
                solutions_list.append((next_st,action1))
                action1=k[1]
                start1=next_st
                break
    solutions_list.reverse()
    return solutions_list

def depth_first_search(start_state,goal_state):
    visited=[]
    stack=[TreeNode(start_state)]
    state_solution=None
    while stack:
        state_check=stack.pop()
        if state_check.val == goal_state:
            visited.append(state_check.val)
            state_solution=state_check
            break
        
        if state_check.val not in visited:
            visited.append(state_check.val)
            for action in actions:
                if generate_next_state(state_check.val,action):
                    state_next = TreeNode(generate_next_state(state_check.val,action),action)
                    state_check.add_child(state_next)
                    stack.append(state_next)

    if not stack:
        return None
    if state_solution:
        list_solution=[(state_solution.val,"These is the solution")]
    while state_solution.parent:
        list_solution.append((state_solution.parent.val,state_solution.move))
        state_solution=state_solution.parent
    list_solution.reverse()
    return list_solution

# Example usage
start_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

## Depth first search
print("Depth-First Search:")
solution_dfs = depth_first_search(start_state, goal_state)
if solution_dfs:
    for step in solution_dfs:
        state, action = step
        print_puzzle(state)
        print("Action:", action)
    print("No. of steps :",len(solution_dfs)-1)
else:
    print("No solution found.")

## Breadth first search
print("Breadth-First Search:")
solution_bfs = breadth_first_search(start_state, goal_state)
if solution_bfs:
    for step in solution_bfs:
        state, action = step
        print_puzzle(state)
        print("Action:", action)
    print("No. of steps :",len(solution_bfs)-1)
else:
    print("No solution found.")
