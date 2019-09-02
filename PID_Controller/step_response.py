# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:31:12 2019
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

# プロセスモデルを作成する。
# 今回は上記のPの関数と、Pade近似の4次を用いて作成する。
G = P * P4
#feedback loopを作成する
sys = matlab.feedback(G*C,1,-1)
print(sys)

"""Step Response"""
time= 100 #step応答を算出する時間[分]
t = np.linspace(0,time,1000) #時間を指定する。
y1,T = matlab.step(G,t)
y2, T = matlab.step(sys,t)
y3 = y1/Kt #y軸のスケールをあわせる為、除する

plt.plot(T, y3, label = "Process")
plt.plot(T, y2, label = "PIDcontroller")
plt.title("Step Response(100)")
plt.xlim((0,time))
plt.ylim((0,2))
plt.xlabel("Time[sec.]")
plt.ylabel("y(t)")
plt.legend()
