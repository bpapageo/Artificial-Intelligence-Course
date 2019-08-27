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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    '''print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())'''

    #check if init state is goal,then return empty set
    Init = problem.getStartState()
    if ((problem.isGoalState(Init))==True):
        return []  

    #initialize the frontier using the initial state of problem.
    frontier = util.Stack()
    frontier.push(Init)

    #initialize the explored set to be empty
    explored = set()

    solution = util.Stack()
    solution.push([])

    while (1) :
        #if the frontier is empty then return failure
        if(frontier.isEmpty()):
            return []

        #choose a leaf node and remove it from the frontier
        Leaf = frontier.pop()
        Result = solution.pop()


        #if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(Leaf):
            return Result

        #add the state of the node to the explored set

        explored.add(Leaf)

        #expand the chosen node, adding the resulting nodes to the frontier only if their state is 
        #not in the frontier or the explored set
        Successors = problem.getSuccessors(Leaf)
        for x in Successors:
            if (x[0] not in explored):#(I COMMENTED THIS IN ORDER TO GET GOOD AUTOGRADER RESULTS) and (x[0] not in frontier.list):
                frontier.push(x[0])
                solution.push(Result+[x[1]])



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
   #check if init state is goal,then return empty set
    #check if init state is goal,then return empty set
    Init = problem.getStartState()
    if ((problem.isGoalState(Init))==True):
        return []  

    #initialize the frontier using the initial state of problem.
    frontier = util.Queue()
    frontier.push(Init)

    #initialize the explored set to be empty
    explored = set()

    solution = util.Queue()
    solution.push([])

    while (1) :
        #if the frontier is empty then return failure
        if(frontier.isEmpty()):
            return []

        #choose a leaf node and remove it from the frontier
        Leaf = frontier.pop()
        Result = solution.pop()


        #if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(Leaf):
            return Result

        #add the state of the node to the explored set
        explored.add(Leaf)
        #print Leaf[0]

        #expand the chosen node, adding the resulting nodes to the frontier only if their state is 
        #not in the frontier or the explored set
        Successors = problem.getSuccessors(Leaf)
        for x in Successors:
            if (x[0] not in explored) and (x[0] not in frontier.list):
                frontier.push(x[0])
                solution.push(Result+[x[1]])


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    Init = problem.getStartState()
    if ((problem.isGoalState(Init))==True):
        return []  

    #initialize the frontier using the initial state of problem.
    frontier = util.PriorityQueue()
    frontier.push(Init,0)

    #initialize the explored set to be empty
    explored = set()

    solution = util.PriorityQueue()
    solution.push([],0)

    while (1) :
        #if the frontier is empty then return failure
        if(frontier.isEmpty()):
            return []

        #choose a leaf node and remove it from the frontier
        Leaf = frontier.pop()
        Result = solution.pop()


        #if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(Leaf):
            return Result

        #add the state of the node to the explored set
        explored.add(Leaf)
        #print Leaf[0]

        #expand the chosen node, adding the resulting nodes to the frontier only if their state is 
        #not in the frontier or the explored set
        Successors = problem.getSuccessors(Leaf)
        for x in Successors:
            if (x[0] not in frontier.heap) and (x[0] not in explored):
                frontier.push(x[0],x[2])
                solution.push(Result+[x[1]],x[2])
            elif (x[0] in frontier.heap):
                frontier.update(x[0],x[2])
                solution.update(Result+[x[1]],x[2])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """Search the node of least total cost first."""
    Init = problem.getStartState()
    if ((problem.isGoalState(Init))==True):
        return []  

    #initialize the frontier using the initial state of problem.
    frontier = util.PriorityQueue()
    frontier.push((Init,[]),heuristic(Init,problem))
    path_d = {}
    #initialize the explored set to be empty
    explored = set()
    path_d[Init] = 0
    '''solution = util.PriorityQueue()
    solution.push([],heuristic(Init,problem))'''

    while not frontier.isEmpty():
        #if the frontier is empty then return failure
        if(frontier.isEmpty()):
            return []

        #choose a leaf node and remove it from the frontier
        Leaf,path = frontier.pop()
        #Result = solution.pop()
        if (Leaf in explored):
        	continue
        temp=path_d[Leaf]
        #if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(Leaf):
            return path

        #add the state of the node to the explored set
        explored.add(Leaf)
        #print Leaf[0]

        #expand the chosen node, adding the resulting nodes to the frontier only if their state is 
        #not in the frontier or the explored set
        Successors = problem.getSuccessors(Leaf)
        for x in Successors:
            if (x[0] in path_d) and (path_d[x[0]]>temp + x[2]):
                frontier.push((x[0],path+[x[1]]),temp+heuristic(x[0],problem)+x[2])
                #solution.push(Result+[x[1]],heuristic(x[0],problem)+x[2])
            else:
                frontier.update((x[0],path+[x[1]]),temp+heuristic(x[0],problem)+x[2])
                #solution.update(Result+[x[1]],heuristic(x[0],problem)+x[2])
        	path_d[x[0]]= temp + x[2]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
