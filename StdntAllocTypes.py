## @file StdntAllocTypes.py
#  @author Nishanth Raveendran
#  @brief Student allocation types
#  @date 11/02/2019

from enum import Enum
from collections import namedtuple
from typing import List
from typing import NamedTuple
from SeqADT import *

## @brief An enumeration representing gender
class GenT(Enum):
    male = 1
    female = 2

## @brief An enumeration representing all departments 
class DeptT(Enum):
    civil = 1
    chemical = 2
    electrical = 3
    mechanical = 4
    software = 5
    materials = 6
    engphys = 7

    
## @brief A named tuple containing all student info (except macid)
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
