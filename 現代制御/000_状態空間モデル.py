# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:10:51 2019
https://algorithm.joho.info/seigyoriron/python-control-state-space-system/
@author: PC
"""

from control.matlab import *

A = "0 1; -1 -1"
B = "0; 1"
C= "2 0"
D = "0"

# 状態空間モデルの作成
sys = ss(A, B, C, D)
print(sys)
