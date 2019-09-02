# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:13:44 2019
https://jp.mathworks.com/help/control/ref/stepinfo.html?searchHighlight=%E6%95%B4%E5%AE%9A%E6%99%82%E9%96%93&s_tid=doc_srchtitle
@author: PC
"""

from control.matlab import *

def main():
  # 伝達関数モデルの作成
    num = [0, 0, 1, 5, 5]     # 分子の係数
    den = [1, 1.65, 5, 6.5, 2]     # 分母の係数
    sys = tf(num, den)  # 伝達関数モデルの作成
    print(sys)
    
    # ステップ応答
    t = np.linspace(0, 10, 1000)
    y, T = step(sys, t)
  
    # 可視化
    plt.plot(T, y)
    plt.grid()
    plt.axhline(1, color="b", linestyle="--")
    plt.xlim(0, 10)
    
    # ステップ応答の特性
    # RiseTime — 応答が定常状態応答の 10% から 90% に達するまでの時間。
    # SettlingTime — 応答 y(t) と定常状態応答 yfinal の誤差 |y(t) - yfinal| が yfinal の 2% 以内に下がるまでの時間。
    # SettlingMin — 応答が立ち上がったときの y (t) の最小値
    # SettlingMax — 応答が立ち上がったときの y (t) の最大値
    # Overshoot — yfinal に対するオーバーシュートの割合
    # Undershoot — アンダーシュートの割合
    # Peak — y (t) のピークの絶対値
    # PeakTime — ピーク値が発生する時間
    S = stepinfo(sys)
    print(S)
    
if __name__ == "__main__":
    main()