# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    print("Start:", startState)
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    from util import Stack
    import time
    fringe = Stack()
    fringe.push((startState, "Start", "None"))
    closed = []
    goalFound = False
    actions = []
    actions2 = Stack()
    while(fringe.isEmpty() == False and goalFound == False):
        loc, direction, parent = fringe.pop()
        actions.append((direction, loc,  parent))        
        if (explored(closed, loc)):
            actions = popUntilParent(parent,actions)
            continue
        closed.append(loc)
        actions = popUntilParentGeneral(parent, actions)
        if problem.isGoalState(loc):
            goalFound = True
        options = problem.getSuccessors(loc)
        for optionLoc, direction, _cost in options:
            fringe.push((optionLoc, direction, loc))
            
        #time.sleep(1.5)
    print(actions)
    return actions
def popUntilParent(loc, actions):
    tempActions = actions
    for _direction, _current, parent in reversed(tempActions):
        tempActions.pop()
        if (parent == loc):
            return tempActions
            
    return tempActions
def popUntilParentGeneral(loc, actions):
    i = 0
    found = False
    tempActions = actions
    print(tempActions)
    print("Location to search for: " + str(loc))
    for _direction, _current, parent in reversed(tempActions):
        i += 1
        if (parent == loc):
            found = True
            break
    print(i)
    if(i >1) and found == True:
        tempActions = popUntilParent(loc, tempActions)    
    return tempActions
    """
    while(temp.isEmpty() == False and found == False):
        direction, parent = temp.pop()
        if (parent[0] == loc[0] and parent[1] == loc[1]):
            found = True
    return temp
    """

def explored(explored, state):
    for location in explored:
        if location[0] == state[0] and location[1] == state[1]:
            return True
    return False

def getDirection(direction):
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    if (direction == 'North'):
        return n
    if (direction == 'South'):
        return s
    if (direction == 'East'):
       return e
    if (direction == 'West'):
        return w

def dfs (problem, state, actions, stack, explored, totalCost):
    from game import Directions
    import util
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    state = problem.getStartState()
    options = problem.getSuccessors(problem.getStartState())
    for option in options:
        stack.push(option)
    print("Stack is:")
    print(stack)
    while stack.isEmpty == False:  
        nextLoc = stack.pop()
        loc = nextLoc[0]
        print(loc)
        direction = nextLoc[1]
        print(direction)
        cost = nextLoc[2]
        print(cost)
        explored.push(loc)
        if (cost > 999999):
            return
        if (explored(explored, state)):
            return
        if (direction == 'North'):
            actions.append(n)
            totalCost += 1
            dfs(problem, state, actions, stack, explored, totalCost)
        if (direction == 'South'):
            actions.append(s)
            totalCost += 1
            dfs(problem, state, actions, stack, explored, totalCost)
        if (direction == 'East'):
            actions.append(e)
            totalCost += 1
            dfs(problem, state, actions, stack, explored, totalCost)
        if (direction == 'West'):
            actions.append(w)
            totalCost += 1
            dfs(problem, state, actions, stack, explored, totalCost)
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
