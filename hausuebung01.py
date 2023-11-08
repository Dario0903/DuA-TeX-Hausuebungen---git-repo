import unittest
from collections import deque

# Hier bitte den Namen und die Matrikelnummer *aller* Gruppenmitglieder eintrage:
# | Name                          | Matrikelnummer
# ---------------------------------------------------------
# | Steffan Wolter                | 10037044
# | Ümit Akbas                    | 2295890
# |                               | 
# |                               | 
 
class Stack(deque):
    """ADT Stack"""

    def top(self):
        return self[-1]
    
    def pop(self):
        return super().pop()
    
    def push(self, e):
        self.append(e)

class Queue(deque):
    """ADT Queue"""

    def front(self):
        return self[0]
    
    def dequeue(self):
        return self.popleft()
    
    def enqueue(self, e):
        self.append(e)


# Aufgabe 2
# DFS mit Hilfe eines Stack


#search int in stack and return if found
def search_stack(stack, int):
    #temp stack
    temp_stack = Stack()
    #boolean for found
    found = False
    #pop stack while stack is not empty
    while stack:
        #pop element from stack
        element = stack.pop()
        #if element is int, return True
        if element == int:
            found = True
        #push element to temp stack
        temp_stack.push(element)
    
    #pop temp stack while temp stack is not empty to restore stack
    while temp_stack:
        #pop element from temp stack
        element = temp_stack.pop()
        #push element to stack
        stack.push(element)
    return found

'''
g = [[0, 2],\
             [0, 1, 2],\
             [0, 1, 2, 3],\
             [0, 1, 2, 3]]
'''

#implement depth first search with stack and the search_stack function
def dfs_tree(graph:list[list[int]], s:int) -> list[list[int]]:
    #create stack
    stack = Stack()
    #start at s and push s to stack
    stack.push(s)
    #




#print graph
def print_graph(graph):
    for i in range(len(graph)):
        print(i, graph[i])

# Aufgabe 3 b) & c)
def zweiteilbar(graph:list[list[int]]) -> (list[int], list[int]):

    #create two sets
    set_a = set()
    set_b = set()

    #loop trough all nodes
    for i in range(len(graph)): # | For-Schleife wird n mal ausgeführt -> O(b)
        #put i in set_a if i is not already in set_b
        if i not in set_b: # | Einzelner Check -> O(1)
            set_a.add(i) # | O(1)
            #loop trough all neighbors of i
            for j in graph[i]: # | For-Schleife wird m mal ausgeführt -> O(m)
                #put j in set_b if j is not already in set_a
                if j not in set_a: # | O(1)
                    set_b.add(j) # | O(1)
                #if j is already in set_a, return None
                else:
                    return None # | O(1)
    return set_a, set_b # | O(1)

# Laufzeit = O(b*m) + O(1) = O(b*m), da n*m = Länge der Kantenliste = Anzahl der Kanten
# Laufzeit = O(n) 

        





# Unit Tests
class TestExercise2(unittest.TestCase):
    def test_bfs_tree1(self):
        g = [[0, 1, 2, 3],\
             [0, 1, 2, 3],\
             [0, 1, 2, 3],\
             [0, 1, 2, 3]]
        g_sol = [[3], [], [1], [2]]

        self.assertEqual(dfs_tree(g, 0), g_sol)

    def test_bfs_tree2(self):
        g = [[0, 2],\
             [0, 1, 2],\
             [0, 1, 2, 3],\
             [0, 1, 2, 3]]
        g_sol = [[2], [], [3], [1]]

        self.assertEqual(dfs_tree(g, 0), g_sol)

    def test_bfs_tree3(self):
        g = [[1, 3],\
             [5],\
             [5],\
             [],\
             [1, 2],\
             [2, 3, 4]]
        g_sol = [[3, 1], [5], [], [], [2], [4]]

        self.assertEqual(dfs_tree(g, 0), g_sol)

class TestExercise3(unittest.TestCase):
    def test_zweiteilbar1(self):
        g = [[0, 1, 2, 3],\
             [0, 1, 2, 3],\
             [0, 1, 2, 3],\
             [0, 1, 2, 3]]

        self.assertIs(zweiteilbar(g), None)

    def test_zweiteilbar2(self):
        g = [[1, 5],\
             [0, 2, 3],\
             [1, 4],\
             [1, 4, 5],\
             [2, 3],\
             [0, 3]]
        A, B = set([0, 2, 3]), set([1, 4, 5])
        a, b = zweiteilbar(g)

        self.assertIn((set(a), set(b)), [(A, B), (B, A)])

if __name__ == '__main__':
    #clear console
    print(chr(27) + "[2J")
    runner = unittest.TextTestRunner()
    print("---------------- Test Exercise 2 ----------------")
    runner.run(unittest.TestLoader().loadTestsFromTestCase(TestExercise2))
    #print("---------------- Test Exercise 3 ----------------")
    #runner.run(unittest.TestLoader().loadTestsFromTestCase(TestExercise3))