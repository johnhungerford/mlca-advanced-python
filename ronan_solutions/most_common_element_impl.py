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
<<<<<<< HEAD
<<<<<<< HEAD
    #I created a dictionary because I wanted to store not only the number of times a value appears, 
    # but also the value itself at the same time
    countPerItem = {}
    #iteration over the list
    for i in List:
            #count the number of times a number appears in the list and attach that as the key to the value that reflects the 
            #original item
            countPerItem.append(i,list.count(i))
        
    #sort through the dictionary to find the item(s) with the largest value
    k=0
    for j in countPerItem.values():
        if j > k: 
            k=j
    
    #find key of items with value k
    rtrnVals = []
    #for l in countPerItem.keys():
        #if countPerItem[l]==k: #this doesn't work but I need to just get the value based on the key. I forget how to implement this as of now, will fix soon
            #rtrnVals.append(l)
    rtrnVals += countPerItem.keys()[countPerItem.index(k)]
    #we return the key(s) associated with this value
=======
=======
>>>>>>> 42284cd85e21cf0a866b17ad88f37c9bdf5091f5
    #Creates a dictionary store the item and the frequency of occurence
    ModeDict = {}
    
    #Iteration over all the items so they can be counted next
    for i in range(len(List)):
        #Count the frequency with which item at index i appears in the list
        ModeDict[List[i]]=List.count(List[i])
<<<<<<< HEAD
=======

    #Combine all the frequencies into a list so can find the greatest
    listkeys=[]
    for i in ModeDict:
        listkeys.append(ModeDict[i])


    for i in listkeys:
        pass
    return None


>>>>>>> 42284cd85e21cf0a866b17ad88f37c9bdf5091f5

    #Combine all the frequencies into a list so can find the greatest
    listkeys=[]
    for i in ModeDict:
        listkeys.append(ModeDict[i])


    for i in listkeys:
        pass
    return None


>>>>>>> 42284cd85e21cf0a866b17ad88f37c9bdf5091f5

    return [rtnrVals]
    #return None
test_most_common_element.run_on(most_common_element)

