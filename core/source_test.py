# -*- coding: utf-8 -*-

import unittest
from wolfox.fengine.extern import * #准备环境
from wolfox.fengine.core.source import *

class ModuleTest(unittest.TestCase):
    def test_normalize_body(self):
        a = [(1,1,1,1,1,1,1),(2,2,2,2,2,2,2),(None,None,None,None,None,None,None),(4,4,4,4,4,4,4)]
        normalize_body(a,0)
        self.assertEquals((2,2,2,2,2,0,0),a[2])

    def test_normalize_head_normal(self):
        a = [(None,None,None,None,None,None,None),(None,None,None,None,None,None,None),(1,1,1,1,1,1,1),(2,2,2,2,2,2,2),(None,None,None,None,None,None,None),(4,4,4,4,4,4,4)]
        ihead = normalize_head(a)
        self.assertEquals(2,ihead)
        self.assertEquals((1,1,1,1,1,0,0),a[0])
        self.assertEquals((1,1,1,1,1,0,0),a[1])

    def test_normalize_head_zero(self):
        a = [(None,None,None,None,None,None,None),(None,None,None,None,None,None,None),(None,None,None,None,None,None,None)]
        ihead = normalize_head(a)
        self.assertEquals(len(a),ihead)
        self.assertEquals((0,0,0,0,0,0,0),a[0])
        self.assertEquals((0,0,0,0,0,0,0),a[1])
        self.assertEquals((0,0,0,0,0,0,0),a[2])

    def test_normalize_head_border(self):
        a = [(None,None,None,None,None,None,None),(None,None,None,None,None,None,None),(1,1,1,1,1,1,1)]
        ihead = normalize_head(a)
        self.assertEquals(2,ihead)
        self.assertEquals((1,1,1,1,1,0,0),a[0])
        self.assertEquals((1,1,1,1,1,0,0),a[1])


if __name__ == "__main__":
    unittest.main()
