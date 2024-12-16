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
from util import *
import time

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

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    start_time = time.time()  # Start the timer
    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    explored = set()

    while not frontier.isEmpty():
        state, path = frontier.pop()

        if problem.isGoalState(state):
            end_time = time.time()  # End the timer
            print(f"DFS: Path Length = {len(path)}, Time Taken = {end_time - start_time:.4f} seconds")
            print(f"Path: {path}")
            return path

        if state not in explored:
            explored.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in explored:
                    frontier.push((successor, path + [action]))

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start_time = time.time()  # Start the timer
    currPath = []  # Path that is popped from the frontier
    currState = problem.getStartState()
    if problem.isGoalState(currState):
        return currPath

    frontier = util.Queue()
    frontier.push((currState, currPath))
    explored = set()

    while not frontier.isEmpty():
        currState, currPath = frontier.pop()
        if problem.isGoalState(currState):
            end_time = time.time()  # End the timer
            print(f"BFS: Path Length = {len(currPath)}, Time Taken = {end_time - start_time:.4f} seconds")
            print(f"Path: {currPath}")
            return currPath

        explored.add(currState)
        frontierStates = [t[0] for t in frontier.list]
        for s in problem.getSuccessors(currState):
            if s[0] not in explored and s[0] not in frontierStates:
                frontier.push((s[0], currPath + [s[1]]))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start_time = time.time()  # Start the timer
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), []), 0)
    explored = set()
    cost_dict = {problem.getStartState(): 0}

    while not frontier.isEmpty():
        state, path = frontier.pop()

        if problem.isGoalState(state):
            end_time = time.time()  # End the timer
            print(f"UCS: Path Length = {len(path)}, Time Taken = {end_time - start_time:.4f} seconds")
            print(f"Path: {path}")
            return path

        if state not in explored:
            explored.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                new_cost = cost_dict[state] + step_cost
                if successor not in cost_dict or new_cost < cost_dict[successor]:
                    cost_dict[successor] = new_cost
                    frontier.push((successor, path + [action]), new_cost)

    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch


