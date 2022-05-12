from itertools import count
from typing import Any, List
from algorithms.dicts.most_common_element import test_most_common_element

def most_common_element(elements: List[Any]) -> List[Any]:
    """
    In a list of values of a given type (any type that can be compared with ==), return
    a list of the most common element values. For instance, in the list [0, 1, 0, 2, 0, 3, 3, 3, 4, 2]
    there are three 0s, three 3s, two 2s, one 1 and one 4, so the correct solution is [0, 3]
    or [3, 0].
    """
    #Creates a dictionary store the item and the frequency of occurence
    ModeDict = {}
    
    #Iteration over all the items so they can be counted next
    for i in range(len(List)):
        #Count the frequency with which item at index i appears in the list
        ModeDict[List[i]]=List.count(List[i])

    #Combine all the frequencies into a list so can find the greatest
    listkeys=[]
    for i in ModeDict:
        listkeys.append(ModeDict[i])


    for i in listkeys:
        pass
    return None



test_most_common_element.run_on(most_common_element)

