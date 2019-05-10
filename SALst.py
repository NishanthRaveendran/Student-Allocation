## @file SALst.py
#  @author Nishanth Raveendran
#  @brief Student Allocation
#  @date 11/02/2019

from StdntAllocTypes import *
from AALst import *
from DCapALst import *

## @brief Student allocation modules
class SALst:

    ## @brief SALst constructor
    #  @details initializes a list for students
    def init():
        SALst.s = []

    ## @brief add adds a student to the list
    #  @param m macid string
    #  @param i SInfoT student info
    def add(m, i):
        for a in SALst.s:
            if m == a[0]:
                raise KeyError
        SALst.s.append((m, i))

    ## @brief remove removes a student from the list
    #  @param m macid of student removed
    def remove(m):
        for x, a in enumerate(SALst.s):
            if m == a[0]:
                del SALst.s[x]
                return
        raise KeyError

    ## @brief elm checks if a student is in the list
    #  @param m macid of student
    #  @return True or False depending on if the student is or isn't included
    def elm(m):
        for a in SALst.s:
            if m == a[0]:
                return True
        return False

    ## @brief info provides the student info from a specified macid
    #  @param m macid 
    #  @return SInfoT of student specified
    def info(m):
        for a in SALst.s:
            if m == a[0]:
                return a[1]
        raise KeyError
        

    ## @brief sort filters and sorts the list of students based on gpa
    #  @details the list is filtered by a specified condition, and the remaining students are sorted based on gpa
    #  @param f sorting condition 
    #  @return list of students that satisfy condition, sorted by gpa
    def sort(f):
        fset = []
        for a in SALst.s:
            if f:
                fset.append(a)
        
        X = sorted(fset, key=lambda i: i.gpa, reverse=True)
        Y = []
        for b in X:
            Y.append(b[0])
        return Y

    ## @brief average finds the gpa average of a filtered list of students
    #  @details the list is filtered by a specified condition, and the average of the remaining students is found
    #  @param f sorting condition 
    #  @return float average of filtered students
    def average(f):
        avg = 0.0
        fset = []
        for a in SALst.s:
            if f:
                fset.append(a)
                avg += a[1].gpa

        if fset == []:
            raise ValueError

        avg /= len(fset)
        return avg
    

    ## @brief allocate allocates the students to their respective departments based on free choice, gpa, and department choices
    #  @details students are filtered and sorted to find the most eligable students, then these students are allocated to a department based on their choices
    def allocate():
        AALst.init()
        F = SALst.sorted(F, lambda t: t.freechoice and t.gpa >= 4.0)
        for a in F:
            ch = a[1].choices
            AALst.add_stdnt(ch.next(), m)

        S = SALst.sorted(S, lambda t: not(t.freechoice) and t.gpa >= 4.0)
        for a in S:
            ch = a[1].choices
            alloc = False
            while not (alloc) and not (ch.end()):
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
                if not(alloc):
                    raise RuntimeError
        

        
