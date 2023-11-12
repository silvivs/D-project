# AED 2 DOGO
# Johnatas Philipe Rodrigues da Silva
# Pedro Henrique Souza dos Santos

# Informed Search implements A* (astar) algorithm 

from heapTools import *

def heuristic(start, goal):
    x1, y1 = start
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def path(origins, current):
    path = [current]
    while current in origins:
        current = origins[current]
        path.append(current)
    path.reverse()
    return path

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

        if current == goal:
            return path(origins, current)

        explored.add(current)

        for neighbor in graph[current]:
            if neighbor in explored:
                continue

            current_g_score = g_score[current] + graph[current][neighbor]

            if current_g_score < g_score[neighbor]:
                origins[neighbor] = current
                g_score[neighbor] = current_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                if neighbor not in [node[1] for node in origins]:
                    insert_element(origins, (f_score[neighbor], neighbor))
    
    return None # when there is no way to the Dogo's food :'(






