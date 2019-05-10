## @file DCapALst.py
#  @author Nishanth Raveendran
#  @brief Department capacity
#  @date 11/02/2019

from StdntAllocTypes import *

## @brief Department capacity allocation modules
class DCapALst:

    ## @brief DCapALst constructor
    #  @details initializes a list for department capacity
    def init():
        DCapALst.s = []

    ## @brief add adds a department and its capacity to the list
    #  @param d DeptT department 
    #  @param n integer capacity
    def add(d, n):
        for i in DCapALst.s:
            if d == i[0]:
                raise KeyError
        DCapALst.s.append((d, n))

    ## @brief remove removes a department from the list
    #  @param d DeptT department
    def remove(d):
        for x, i in enumerate(DCapALst.s):
            if d == i[0]:
                del DCapALst.s[x]
                return
        raise KeyError

    ## @brief elm checks if a department is in the list
    #  @param d DeptT department 
    #  @return True or False depending on if the department is or isn't included
    def elm(d):
        for i in DCapALst.s:
            if d == i[0]:
                return True
        return False

    ## @brief capacity gives the capacity of a specified department
    #  @param d DeptT department 
    #  @return integer capacity of specified department
    def capacity(d):
        for i in DCapALst.s:
            if d == i[0]:
                return i[1]
        raise KeyError