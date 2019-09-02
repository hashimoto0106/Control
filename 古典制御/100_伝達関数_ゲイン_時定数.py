# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:15:20 2019
https://qiita.com/hikaruyaku/items/021769a76e72ed34a881
@author: PC
"""

from control import matlab

Kt = 10  # Steady-State gain
J = 25  # Time Constant
Cm = 4  # Dead time ここでは使用しない
num = [Kt]  # 分子の係数
dem = [J, 1]  # 分母の係数

P = matlab.tf(num, dem)
print(P)
