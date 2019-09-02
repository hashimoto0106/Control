# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:16:59 2019
https://qiita.com/nnn112358/items/168e507a34272957b1f3
@author: PC
"""

from control.matlab import *    # MATLAB-like functions

# System matrics
A1 = [[0, 1.], [-4, -1]]
B1 = [[0], [1.]]
C1 = [[1., 0]]
sys1ss = ss(A1, B1, C1, 0)
print(sys2ss)

sys1tf = ss2tf(sys1ss)
print(sys2tf)