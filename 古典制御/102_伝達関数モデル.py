# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:10:46 2019

@author: PC
"""

from control.matlab import *

def main():
  # 伝達関数モデルの作成
  G = tf([1], [1., 3])
  print(G)
  
if __name__ == "__main__":
    main()
