from heapsort import heapsort

class Element:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __str__(self):
        return str(self.value) + " " + str(self.priority)
    
    def __lt__(self, other):
        return self.priority < other.priority
    
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []
    
    def size(self):
        return len(self.elements)
    
    def insert(self, value, priority):
        self.elements.append(Element(value, priority))
        print("Element inserted: ", value, priority)

    def remove(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Removing element with highest priority")
            heapsort(self.elements)
            highest_priority = 0
            removed = self.elements.pop(highest_priority)

            return removed.value
        
    def print_queue(self):
        output = []
        for element in self.elements:
            output.append(element.value)
        print(output)