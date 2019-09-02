# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:15:24 2019
https://qiita.com/nnn112358/items/168e507a34272957b1f3
@author: PC
"""

from control.matlab import *    # MATLAB-like functions

# 伝達関数
sys2tf = tf([1, 0.5], [1, 5]);
print(sys2tf)

# 状態方程式
sys2ss = tf2ss(sys2tf);
print(sys2ss)
