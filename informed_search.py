from priority_queue import PriorityQueue as PQ

def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])


class informedSearch:
    def __init__(self):
        self.agenda = PQ()
        self.visited = set()

    def search(self, initialState):
        state = initialState()
        priotity = 0
        self.agenda.insert(state, 0)
