# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:47:05 2019

@author: PC
"""


from control.matlab import *

def main():
  # 伝達関数モデルの作成
  G = tf([1], [1., 3])
  print(G)
  
  P = tf([1], [1., 3])
  print(P)
  
  print(feedback(G,P))
if __name__ == "__main__":
    main()
