## @file Read.py
#  @author Nishanth Raveendran
#  @brief Reads student and department text files
#  @date 11/02/2019

from StdntAllocTypes import *
from DCapALst import *
from SALst import *

## @brief Reads text files for students and department capacities
class Read:

    ## @brief load_student_data creates a list of students based on information from a text file
    #  @details the textfile contain a line of information for each student, and this module converts that into malleable data
    #  @param s textfile containing information of students
    def load_student_data(s):
        SALst.init()

        with open(s, 'r') as stdnt_data:
            for line in stdnt_data:
                D = line.split(",")
                
                if D[3] == "male":
                    D[3] = GenT.male
                else:
                    D[3] = GenT.female

                D[4] = float(D[4])

                if D[-1] == "True":
                    D[-1] = True
                else:
                    D[-1] = False

                D[5] = D[5][1:]
                D[-2] = D[-2][:-1]

                C = []
                for i in range(5, len(D) - 1):
                    if D[i] == "civil":
                        D[i] = DeptT.civil
                    elif D[i] == "chemical":
                        D[i] = DeptT.chemical
                    elif D[i] == "electrical":
                        D[i] = DeptT.chemical
                    elif D[i] == "mechanical":
                        D[i] = DeptT.chemical
                    elif D[i] == "software":
                        D[i] = DeptT.chemical
                    elif D[i] == "materials":
                        D[i] = DeptT.chemical
                    elif D[i] == "engphys":
                        D[i] = DeptT.engphys

                    C.append(D[i])

                SALst.add(D[0], SInfoT(D[1], D[2], D[3], D[4], SeqADT(C), D[-1]))       
               

    ## @brief load_dcap_data loads the department capacities 
    #  @details reads a textfile containing the capacities of each department, and converting it into a list 
    #  @param s textfile containing department capacities
    def load_dcap_data(s):
       DCapALst.init()

       with open(s, 'r') as dept_capacity:
           for line in dept_capacity:
                dep, cap = line.split(",")
                if dep == "civil":
                    dep = DeptT.civil
                elif dep == "chemical":
                    dep = DeptT.chemical
                elif dep == "electrical":
                    dep = DeptT.chemical
                elif dep == "mechanical":
                    dep = DeptT.chemical
                elif dep == "software":
                    dep = DeptT.chemical
                elif dep == "materials":
                    dep = DeptT.chemical
                elif dep == "engphys":
                    dep = DeptT.engphys
               
                cap = int(cap)

                DCapALst.add(dep, cap)

            