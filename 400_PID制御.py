# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:09:15 2019

@author: PC
"""

from control.matlab import *
from matplotlib import pyplot as plt
import numpy as np

def main():
  # PID制御器のパラメータ
  Kp = 0.6  # 比例
  Ki = 0.03 # 積分
  Kd = 0.03 # 微分
  num = [Kd, Kp, Ki]
  den = [1, 0]
  K = tf(num, den)
  print(K)

  # 制御対象
  Kt = 1
  J = 0.01
  C = 0.1
  num = [Kt]
  den = [J, C, 0]
  G = tf(num, den)
  print(G)

  # フィードバックループ
  sys = feedback(K*G, 1)
  t = np.linspace(0, 3, 1000)
  y, T = step(sys, t)
  
  # 可視化
  plt.plot(T, y)
  plt.grid()
  plt.axhline(1, color="b", linestyle="--")
  plt.xlim(0, 3)
  
if __name__ == "__main__":
  main()
