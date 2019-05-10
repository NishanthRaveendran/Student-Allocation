from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from SALst import *
from pytest import *

class TestSeqADT:

    def test_next(self):
        S = SeqADT([DeptT.engphys, DeptT.electrical])
        assert S.next() == DeptT.engphys
        assert S.next() == DeptT.electrical

    def test_next_raises_StopIteration(self):
        S = SeqADT([])
        with raises(StopIteration):
            S.next()

    def test_end_T(self):
        S = SeqADT([])
        assert S.end()

    def test_end_F(self):
        S = SeqADT([DeptT.engphys, DeptT.electrical])
        assert not S.end()

class TestDCapALst:

    def test_init(self):
        DCapALst.init()
        assert DCapALst.s == []

    def test_add(self):
        DCapALst.add(DeptT.engphys, 9)
        DCapALst.add(DeptT.electrical, 7)
        assert DCapALst.s == [(DeptT.engphys, 9), (DeptT.electrical, 7)]

    def test_remove(self):
        DCapALst.remove(DeptT.engphys)
        assert DCapALst.s == [(DeptT.electrical, 7)]

    def test_remove_raises_KeyError(self):
        with raises(KeyError):
            DCapALst.remove(DeptT.software)

    def test_elm(self):
        assert DCapALst.elm(DeptT.electrical)
        assert not DCapALst.elm(DeptT.chemical)

    def test_capacity(self):
        assert DCapALst.capacity(DeptT.electrical) == 7
        assert DCapALst.capacity(DeptT.electrical) != 3
    
    def test_capacity_raises_KeyError(self):
        with raises(KeyError):
            DCapALst.capacity(DeptT.civil)


class TestSALst:
    s1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
    s2 = SInfoT("tory", "lory", GenT.female, 5.9, SeqADT([DeptT.software, DeptT.civil]), False)
    s3 = SInfoT("Charlie", "Brown", GenT.male, 3.1, SeqADT([DeptT.engphys, DeptT.software, DeptT.chemical, DeptT.materials]), True)
    s4 = SInfoT("John", "Smith", GenT.male, 7.1, [DeptT.mechanical, DeptT.electrical, DeptT.materials, DeptT.mechanical, DeptT.electrical], True)
    X1 = [("macid", s1), ("jane", s2)]
    X2 = [("jane", s2)]
    S1 = [("macid", s1), ("jsmith", s4), ("jane", s2), ("brownc", s3)]
    S2 = [("macid", s1), ("jsmith", s4)]
    
    def test_init(self):
        SALst.init()
        assert SALst.s == []

    def test_add(self):
        SALst.add("macid", TestSALst.s1)
        SALst.add("jane", TestSALst.s2)
        assert SALst.s != []
        assert SALst.s == TestSALst.X1

    def test_add_raises_KeyError(self):
        with raises(KeyError):
            SALst.add("macid", TestSALst.s1)

    def test_remove(self):
        SALst.remove("macid")
        assert SALst.s == TestSALst.X2

    def test_remove_raises_KeyError(self):
        with raises(KeyError):
            SALst.remove("tony")

    def test_elm(self):
        assert SALst.elm("jane")
        assert not SALst.elm("macid")

    def test_info(self):
        assert SALst.info("jane") == TestSALst.s2
    
    def test_info_raises_KeyError(self):
        with raises(KeyError):
            SALst.info("tony")

    def test_sort_all(self):
        SALst.add("macid", TestSALst.s1)
        SALst.add("brownc", TestSALst.s3)        
        SALst.add("jsmith", TestSALst.s4)

        SALst.sort(True)
        assert SALst.s == TestSALst.S1
