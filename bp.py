# -*- coding:utf-8 -*-
from __future__ import division
import numpy as np
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0],[1,0,0,1]]).T
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,4)) -1
syn2 = 2*np.random.random((4,2)) - 1
for j in xrange(60000):
    z1 = np.dot(X, syn0)
    l1 = 1/(1+np.exp(-(z1)))
    z2 = np.dot(l1, syn1)
    l2 = 1/(1+np.exp(-(z2)))
    z3 = np.dot(l2, syn2)
    l3 = 1 / (1 + np.exp(-(z3)))
    l3_delta = (y-l3)*(l3*(1-l3))
    l2_delta = l3_delta.dot(syn2.T)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)

l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
l3 = 1/(1+np.exp(-(np.dot(l2,syn2))))



print(l3.T)