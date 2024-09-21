from collections import deque
from functools import total_ordering


## We will append tuples (state, "action") in the search queue
## Parameters: s, action_list, mission_complete
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    total_states1 = 0
    search_queue = deque()
    closed_list = {}

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        if goal_test(next_state[0]):
            # print("Goal found")
            # print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                # print(ptr)
            return next_state, total_states1
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    total_states1 += 1
                    closed_list[s[0]] = True
            search_queue.extend(successors)

### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, limit=0, use_closed_list=True) :
    total_states2 = 0
    search_queue = deque()
    closed_list = {}

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            # print("Goal found")
            # print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                # print(ptr)
            return next_state, total_states2
        else :
            # since depth is added in successor func, need to verify that current depth + 1 won't exceed limit
            if next_state[0].depth + 1 <= limit or limit == 0 :
                successors = next_state[0].successors(action_list)
                if use_closed_list :
                    successors = [item for item in successors
                                        if item[0] not in closed_list]
                    for s in successors :
                        total_states2 += 1
                        closed_list[s[0]] = True
                search_queue.extend(successors)

