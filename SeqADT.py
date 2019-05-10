## @file SeqADT.py
#  @author Nishanth Raveendran
#  @brief SeqADT - abstract data type for choices
#  @date 11/02/2019

## @brief An abstract data type that represents a list of department choices 
class SeqADT:

    ## @brief SeqADT constructor
    #  @details takes a list of departments and makes it a more restricted data type
    #  @param x list of DeptT departments
    def __init__(self, x):
        self.__s = x
        self.__i = 0

    ## @brief start sets the index of the list at 0
    def start(self):
        self.__i = 0

    ## @brief next presents the current department and iterates to the next department in the list
    #  @return current DeptT department
    def next(self):
        if self.__i >= len(self.__s): 
            raise StopIteration
        self.__i += 1
        return self.__s[self.__i - 1]

    ## @brief end checks if you have iterated through the whol SeqADT
    #  @return boolean value depending on if it is or isnt at the end of the SeqADT
    def end(self):
        return self.__i >= len(self.__s)