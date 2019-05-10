## @file AALst.py
#  @author Nishanth Raveendran
#  @brief Department allocator 
#  @date 11/02/2019

from StdntAllocTypes import *

## @brief Department allocation modules
class AALst:

    ## @brief AALst constructor
    #  @details initializes a list of tuples representing each department and the students in the department
    def init():
        AALst.s = [(DeptT.civil, []), (DeptT.chemical, []), (DeptT.electrical, []), (DeptT.mechanical, []), (DeptT.software, []), (DeptT.materials, []), (DeptT.engphys, [])]

    ## @brief add_stdnt adds a student to a specified department
    #  @param dep DeptT department 
    #  @param m macid of a student
    def add_stdnt(dep, m):
        for i in AALst.s:
            if i[0] == dep:
                i[1].append(m)

    ## @brief lst_alloc gives the list of students for a specified department
    #  @param d DeptT department 
    #  @return list of macids of students
    def lst_alloc(d):
        for i in AALst.s:
            if i[0] == d:
                return i[1]

    ## @brief num_alloc gives the number of students in a specified department
    #  @param d DeptT department 
    #  @return number of students in department
    def num_alloc(d):
        return len(AALst.lst_alloc(d))