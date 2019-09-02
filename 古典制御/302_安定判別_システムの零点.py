# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:09:15 2019

@author: PC
"""

from control.matlab import *

def main():
  A = "0 1; -1 -1"
  B = "0; 1"
  C= "2 0"
  D = "0"
  # 状態空間モデルの作成
  sys = ss(A, B, C, D)
  zeros = zero(sys)
  print(zeros)


if __name__ == "__main__":
    main()
