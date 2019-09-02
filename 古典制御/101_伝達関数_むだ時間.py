# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:15:20 2019
https://qiita.com/hikaruyaku/items/021769a76e72ed34a881
@author: PC
"""

from control import matlab
import numpy as np

Kt = 10  # Steady-State gain
J = 25  # Time Constant
Cm = 4  # Dead time ここでは使用しない
num = [Kt]  # 分子の係数
dem = [J, 1]  # 分母の係数

P = matlab.tf(num, dem)

#pade近似を表現,前提として5秒のむだ時間を設定
#まずパデ近似の分子、分母を求める
num2, dem2 = matlab.pade(5,2)
num4, dem4 = matlab.pade(5,4)
num6, dem6 = matlab.pade(5,6)
num8, dem8 = matlab.pade(5,8)
num10, dem10 = matlab.pade(5,10)
#pade近似の分子、分母を伝達関数の形に変換
P2 = matlab.tf(num2,dem2)
P4 = matlab.tf(num4,dem4)
P6 = matlab.tf(num6,dem6)
P8 = matlab.tf(num8,dem8)
P10 = matlab.tf(num10,dem10)
#最後にstep応答を行う
time= 100
t = np.linspace(0,time,1000)
y2,T = matlab.step(P2,t)
y4,T = matlab.step(P4,t)
y6,T = matlab.step(P6,t)
y8,T = matlab.step(P8,t)
y10,T = matlab.step(P10,t)
#結果の表示
from matplotlib import pylab as plt
plt.plot(T, y2, label = "2")
plt.plot(T, y4, label = "4")
plt.plot(T, y6, label = "6")
plt.plot(T, y8, label = "8")
plt.plot(T, y10, label = "10")
plt.xlim((1,15))
plt.ylim((-0.50,1.1))
plt.xlabel("Time[sec.]")
plt.ylabel("y(t)")
plt.legend()

print(P)
