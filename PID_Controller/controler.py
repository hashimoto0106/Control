# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:30:06 2019
https://qiita.com/hikaruyaku/items/021769a76e72ed34a881
@author: PC
"""

from control import matlab

K = 0.75  # Proprotional Gain
Ti = 8  # Integral Time
Td = 2  # Derivarive Time

# 伝達関数用の係数に変換
kp = K
ki = kp/Ti
kd = Td * kp
num = [kd, kp, ki]
den = [1, 0]

C = matlab.tf(num, den)
print(C)
