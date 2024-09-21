## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
# Rover should travel from station -> sample -> station -> charger
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search, depth_first_search


class RoverState :
    def __init__(self, loc="station", sample_extracted=False, holding_sample=False, charged=False, holding_tool=False, complete=False, depth=0):
        self.loc = loc
        self.sample_extracted = sample_extracted
        self.holding_sample = holding_sample
        self.charged = charged
        self.holding_tool = holding_tool
        self.complete = complete
        self.depth = depth
        self.prev = None

    ## you do this.
    def __eq__(self, other):
        return (self.loc == other.loc and
                self.sample_extracted == other.sample_extracted and
                self.holding_sample == other.holding_sample and
                self.charged == other.charged and
                self.holding_tool == other.holding_tool and
                self.complete == other.complete)

    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}\n" +
                f"Holding Tool?: {self.holding_tool}\n" +
                f"Completed?: {self.complete}\n" +
                f"Depth: {self.depth}")

    def __str__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n" +
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}")

    def __hash__(self):
        return self.__str__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        self.depth += 1
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev=state
    return r2
def move_to_station(state) :
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2

def pick_up_tool(state) :
    r2 = deepcopy(state)
    r2.holding_tool = True
    r2.prev = state
    return r2

def drop_tool(state) :
    r2 = deepcopy(state)
    r2.holding_tool = False
    r2.prev = state
    return r2

def use_tool(state) :
    r2 = deepcopy(state)
    r2.sample_extracted = True
    r2.prev = state
    return r2

def pick_up_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "station":
        r2.holding_sample = False
        r2.complete = True
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "battery":
        r2.charged = True
    r2.prev = state
    return r2


action_list = [charge, drop_sample, pick_up_sample,
               move_to_sample, move_to_battery, move_to_station,
               pick_up_tool, drop_tool, use_tool]

def battery_goal(state) :
    return state.loc == "battery"
## add your goals here.
def sample_goal(state) :
    return state.loc == "sample"
def station_goal(state) :
    return state.loc == "station"

# return true if we are at the battery, charged, and the sample is at the station
def mission_complete(state) :
    return (state.loc == "battery" and
            state.charged and
            state.sample_extracted and
            state.complete and
            state.holding_sample == False)

# return true if we are at the sample
def moveToSample(state) :
    return (state.loc == "sample" and
            not state.charged and
            not state.holding_sample and
            not state.sample_extracted and
            not state.holding_tool)


# return true if we have extracted the sample
def removeSample(state) :
    return (state.loc == "sample" and
            state.sample_extracted and
            state.holding_sample and
            not state.charged)

# return true if we have returned to the charger
def returnToCharger(state) :
    return (state.loc == "battery" and
            state.charged)



if __name__=="__main__" :
    s = RoverState()
    print("General \"mission_complete\" Solutions")
    result1, total1 = breadth_first_search(s, action_list, mission_complete)
    print("Breadth First Search\nResult: %r\nTotal States: %d\n" % (result1, total1))
    result2, total2 = depth_first_search(s, action_list, mission_complete)
    print("Depth First Search\nResult: %r\nTotal States: %d\n" % (result2, total2))
    result3, total3 = depth_first_search(s, action_list, mission_complete, 6)
    print("Depth Limited Search with depth-limit: 7\nResult: %r\nTotal States: %d\n" % (result3, total3))

    # Adjusting with the new subgoals
    print("\"moveToSample\" Solutions")
    result4, total4 = breadth_first_search(s, action_list, moveToSample)
    print("Breadth First Search\nResult: %r\nTotal States: %d\n" % (result4, total4))
    result5, total5 = depth_first_search(s, action_list, moveToSample)
    print("Depth First Search\nResult: %r\nTotal States: %d\n" % (result5, total5))
    result6, total6 = depth_first_search(s, action_list, moveToSample, 6)
    print("Depth Limited Search with depth-limit: 7\nResult: %r\nTotal States: %d\n" % (result6, total6))

    # changing start state
    s.loc = "sample"

    print("\"removeSample\" Solutions")
    result7, total7 = breadth_first_search(s, action_list, removeSample)
    print("Breadth First Search\nResult: %r\nTotal States: %d\n" % (result7, total7))
    result8, total8 = depth_first_search(s, action_list, removeSample)
    print("Depth First Search\nResult: %r\nTotal States: %d\n" % (result8, total8))
    result9, total9 = depth_first_search(s, action_list, removeSample, 10)
    print("Depth Limited Search with depth-limit: 10\nResult: %r\nTotal States: %d\n" % (result9, total9))

    # changing start state
    s.holding_sample = True
    s.sample_extracted = True


    print("\"returnToCharger\" Solutions")
    result10, total10 = breadth_first_search(s, action_list, returnToCharger)
    print("Breadth First Search\nResult: %r\nTotal States: %d\n" % (result10, total10))
    result11, total11 = depth_first_search(s, action_list, returnToCharger)
    print("Depth First Search\nResult: %r\nTotal States: %d\n" % (result11, total11))
    result12, total12 = depth_first_search(s, action_list, returnToCharger, 16)
    print("Depth Limited Search with depth-limit: 16\nResult: %r\nTotal States: %d\n" % (result12, total12))






