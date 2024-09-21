# Stephanie Pena

from mars_planner import *
from routefinder import *

if __name__=="__main__" :
    s = RoverState()
    print("-------------General \"mission_complete\" Solutions-------------")
    result1, total1 = breadth_first_search(s, action_list, mission_complete)
    print("Breadth First Search\nResult: %r\nTotal States: %d\n" % (result1, total1))
    result2, total2 = depth_first_search(s, action_list, mission_complete)
    print("Depth First Search\nResult: %r\nTotal States: %d\n" % (result2, total2))
    result3, total3 = depth_first_search(s, action_list, mission_complete, 6)
    print("Depth Limited Search with depth-limit: 7\nResult: %r\nTotal States: %d\n" % (result3, total3))

    # Adjusting with the new subgoals
    print("-------------\"moveToSample\" Solutions-------------")
    result4, total4 = breadth_first_search(s, action_list, moveToSample)
    print("Breadth First Search\nResult: %r\nTotal States: %d\n" % (result4, total4))
    result5, total5 = depth_first_search(s, action_list, moveToSample)
    print("Depth First Search\nResult: %r\nTotal States: %d\n" % (result5, total5))
    result6, total6 = depth_first_search(s, action_list, moveToSample, 6)
    print("Depth Limited Search with depth-limit: 7\nResult: %r\nTotal States: %d\n" % (result6, total6))

    # changing start state
    s.loc = "sample"

    print("-------------\"removeSample\" Solutions-------------")
    result7, total7 = breadth_first_search(s, action_list, removeSample)
    print("Breadth First Search\nResult: %r\nTotal States: %d\n" % (result7, total7))
    result8, total8 = depth_first_search(s, action_list, removeSample)
    print("Depth First Search\nResult: %r\nTotal States: %d\n" % (result8, total8))
    result9, total9 = depth_first_search(s, action_list, removeSample, 10)
    print("Depth Limited Search with depth-limit: 10\nResult: %r\nTotal States: %d\n" % (result9, total9))

    # changing start state
    s.holding_sample = True
    s.sample_extracted = True


    print("-------------\"returnToCharger\" Solutions-------------")
    result10, total10 = breadth_first_search(s, action_list, returnToCharger)
    print("Breadth First Search\nResult: %r\nTotal States: %d\n" % (result10, total10))
    result11, total11 = depth_first_search(s, action_list, returnToCharger)
    print("Depth First Search\nResult: %r\nTotal States: %d\n" % (result11, total11))
    result12, total12 = depth_first_search(s, action_list, returnToCharger, 16)
    print("Depth Limited Search with depth-limit: 16\nResult: %r\nTotal States: %d\n" % (result12, total12))


    print("-------------\"routefinder\" Solutions-------------")
    graph = read_mars_graph('MarsMap')
    map = map_state("8,8", graph)
    result13, total13 = a_star(map, sld, mission_compl)
    print("A* Search\nResult: %r\nTotal States: %d\n" % (result13, total13))
    result14, total14 = a_star(map, h1, mission_compl)
    print("Uniform Cost Search\nResult: %r\nTotal States: %d\n" % (result14, total14))
