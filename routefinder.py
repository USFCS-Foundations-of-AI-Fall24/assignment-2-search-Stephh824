import math
from queue import PriorityQueue
from Graph import *


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'

    def successors(self) :
        successors = []
        # get current location from the state
        node = Node(self.location)
        edges = self.mars_graph.get_edges(node)
        for edge in edges :
            nmap = map_state(edge.dest, self.mars_graph, self, self.g + 1)
            successors.append(nmap)
        return successors
    # 	use the graph (mars_graph) to find the neighbors (which has the get_edges method)
    # 	for each edge
    # 		create a mapstate class
    # 			set the g and h properly
    # 		enqueue


def mission_complete(state) :
    return state.is_goal()

# heuristic_fn is either h1 or sld
# goal_test is going to be "g, g"
def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    total_states = 0
    heuristic = heuristic_fn(start_state)
    start_state.h = heuristic
    start_state.f = start_state.g + start_state.h
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)

    if use_closed_list :
        closed_list[start_state] = True
    while search_queue.qsize() > 0 : # CHANGE

        next_state = search_queue.get()
        if goal_test(next_state) :
            print("Goal found")
            # print(next_state)
            return next_state, total_states
        else :
            successors = next_state.successors()
            if use_closed_list :
                successors = [item for item in successors if item not in closed_list]
                for s in  successors :
                    total_states += 1
                    heuristic = heuristic_fn(s)
                    s.h = heuristic
                    s.f = s.g + s.h
                    closed_list[s] = True
                    search_queue.put(s)



## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
# sqrt( (x1 - x2)^2 + (y1 - y2)^2 ) where (x2, y2) = (1,1)
def sld(state) :
    cord = state.location.split(",")
    dist = math.sqrt( ((int(cord[0]) - 1) ** 2) + ((int(cord[1]) - 1) ** 2) )
    return dist


## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    lines = sum(1 for line in open(filename))
    mars_graph = Graph(lines)
    with open(filename) as f :
        for line in f.readlines() :
            line1 = line.strip('\n').split(":")
            node1 = Node(line1[0])
            mars_graph.add_node(node1)
            for edges in line1[1].lstrip(" ").split(" ") :
                edge1 = Edge(node1, edges)
                mars_graph.add_edge(edge1)
    return mars_graph

if __name__ == '__main__' :
    graph = read_mars_graph('MarsMap')
    map = map_state("8,8", graph)
    result, states = a_star(map, sld, mission_complete)
    print("A* Search\nResult: %r\nTotal States: %d\n" % (result, states))
    result1, states1 = a_star(map, h1, mission_complete)
    print("Uniform Cost Search\nResult: %r\nTotal States: %d\n" % (result1, states1))

