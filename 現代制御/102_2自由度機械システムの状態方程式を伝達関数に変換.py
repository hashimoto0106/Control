# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:16:59 2019
https://algorithm.joho.info/seigyoriron/python-control-ss2tf-2-degrees-of-freedom-mechanical-system/
@author: PC
"""
def main():
    # マス・ダンパ・バネの係数
    m1, m2 = 1.0, 1.2
    d1, d2 = 0.1, 0.2
    k1, k2 = 1.0, 1.5    
    
    # 状態方程式の行列
    A = [[0., 1, 0, 0],
         [-(k1+k2)/m1,  -(d1+d2)/m1, -k2/m1 ,-d2/m1],
         [0., 0., 0., 1.],
         [-k2/m2, d2/m2, -k2/m2, -d2/m2] ]
    B = [[0.],
         [0.],
         [0.],
         [1./m2]]
    C = [[0., 0., 1., 0.]]
    D = [[0.]]
    
    # 状態方程式から伝達関数を求める
    sys_tf = ss2tf(A, B, C, D)
    print(sys_tf)

if __name__ == "__main__":
    main()
