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
    return [s, s, w, s, w, w, s, w]


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
    from util import Stack
    # Set up stack and starting states
    fringe = Stack()
    startState = problem.getStartState()
    fringe.push((startState, "Start", startState))
    closed = []
    goalFound = False
    actions = [(startState, startState)]
    # Itterate through stack until empty or goal found
    while(fringe.isEmpty() == False and goalFound == False):
        # Pop info from fringe
        loc, direction, parent = fringe.pop()
        # ignore visited nodes
        if (loc in closed):
            continue
        # pop back solution to past parent
        actions = popUntilParent(parent, actions)
        actions.append((loc, direction))
        if problem.isGoalState(loc):
            goalFound = True
            break
        closed.append(loc)
        # Get successors
        options = problem.getSuccessors(loc)
        for optionLoc, direction, _cost in options:
            if (optionLoc not in closed):
                fringe.push((optionLoc, direction, loc))
    # Pop initial setup nodes
    if (goalFound == False):
        raise Exception('Goal Not Found, Failure')
    print(actions)
    # Remove starting state actions (dummy actions for the list)
    actions.pop(0)
    actions.pop(0)
    # Convert takes only the direction
    path = []
    for _loc, direction in actions:
        path.append(direction)
    print(path)
    return path


def popUntilParent(loc, actions):
    try:
        while (actions[-1][0] != loc):
            actions.pop()
    except:
        pass
    finally:
        return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    # Set up stack and starting states
    fringe = Queue()
    startState = problem.getStartState()
    fringe.push((startState, "Start", startState))
    closed = []
    goalFound = False
    goal = (0, 0, 0)
    actions = {}
    # Itterate through stack until empty or goal found
    while(fringe.isEmpty() == False and goalFound == False):
        # Pop info from fringe
        loc, direction, parent = fringe.pop()
        # ignore visited nodes
        if (loc in closed):
            continue
        actions[loc] = (parent, direction)
        if problem.isGoalState(loc):
            goalFound = True
            goal = (loc, direction, parent)
            break
        closed.append(loc)
        # Get successors
        options = problem.getSuccessors(loc)
        for optionLoc, direction, _cost in options:
            if (optionLoc not in closed):
                fringe.push((optionLoc, direction, loc))
    # Pop initial setup nodes
    if (goalFound == False):
        raise Exception('Goal Not Found, Failure')

    # Convert actions to a direction
    path = []
    goal = goal[0]
    temp = actions[goal]
    # find the parent of the state until the start
    while temp[0] != startState:
        direction = temp[1]
        parent = temp[0]
        path.append(direction)
        temp = actions[parent]
    # append the remaining direction
    path.append(temp[1])
    # Reverse the path to get the directions from the start instead of the goal
    path.reverse()
    return path


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    # Set up stack and starting states
    fringe = PriorityQueue()
    startState = problem.getStartState()
    fringe.push((startState, "Start", startState, 0), 0)
    closed = []
    goalFound = False
    goal = (0, 0, 0, 0)
    actions = {}
    # Itterate through stack until empty or goal found
    while(fringe.isEmpty() == False and goalFound == False):
        # Pop info from fringe
        loc, direction, parent, cost = fringe.pop()
        # ignore visited nodes
        if (loc in closed):
            continue
        actions[loc] = (parent, direction)
        if problem.isGoalState(loc):
            goalFound = True
            goal = (loc, direction, parent)
            break
        closed.append(loc)
        # Get successors
        options = problem.getSuccessors(loc)
        for optionLoc, direction, optionCost in options:
            if (optionLoc not in closed):
                fringe.push((optionLoc, direction, loc,
                             optionCost + cost), optionCost+cost)
    # Pop initial setup nodes
    if (goalFound == False):
        raise Exception('Goal Not Found, Failure')

    # Convert actions to a direction
    path = []
    goal = goal[0]
    temp = actions[goal]
    # find the parent of the state until the start
    while temp[0] != startState:
        direction = temp[1]
        parent = temp[0]
        path.append(direction)
        temp = actions[parent]
    # append the remaining direction
    path.append(temp[1])
    # Reverse the path to get the directions from the start instead of the goal
    path.reverse()
    return path


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
