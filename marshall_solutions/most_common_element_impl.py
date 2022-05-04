from typing import Any, List
from algorithms.dicts.most_common_element import test_most_common_element

def most_common_element(elements: List[Any]) -> List[Any]:
    """
    In a list of values of a given type (any type that can be compared with ==), return
    a list of the most common element values. For instance, in the list [0, 1, 0, 2, 0, 3, 3, 3, 4, 2]
    there are three 0s, three 3s, two 2s, one 1 and one 4, so the correct solution is [0, 3]
    or [3, 0].
    """
    vals = {}
    most_common = 0
    list_vals = []
    
    for element in elements:
        if element in vals:
            vals[element] += 1
            
        else:
            vals[element] = 1

    for element in vals:
        if vals[element] > most_common:
            most_common = vals[element]
            list_vals = [element]
            
        elif vals[element] == most_common:
            list_vals.append(element)         
                       
            
    return list_vals

test_most_common_element.run_on(most_common_element)
