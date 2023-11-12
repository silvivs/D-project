
# AED 2 DOGO
# Johnatas Philipe Rodrigues da Silva
# Pedro Henrique Souza dos Santos

# Informed Search implements A* (astar) algorithm 

from heapTools import *

def heuristic(start, goal):
    x1, y1 = start
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def astar(graph, start, goal):
    toExplore = []
    explored = set()
    origins = {}

    # this create a dictionary: distance from start to each node
    g_score = {node: float('inf') for node in graph} 
    g_score[start] = 0

    # this create a dictionary: distance from start to goal
    f_score = {node: float('inf') for node in graph} 
    f_score[start] = heuristic(start, goal)

    # insert the first node to explore
    insert_element(toExplore, (f_score[start], start))

    while toExplore:
        current = pop_min(toExplore)[1] # Accessing the second element of the tuple (the cost estimate f_score)
        

