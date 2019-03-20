# -*- coding:utf-8 -*- 
__author__ = 'xuy'

# -*- coding: UTF-8 -*-


import numpy as np

#relu的函数：当x>0的时候函数是x,当x小于0时函数是0
#因此求导数之后，当x大于０的时候，导数为１，否则当x小于０的时候导数为０
class ReluActivator(object):
    def forward(self, weighted_input):
        #return weighted_input
        return max(0, weighted_input)

    def backward(self, output):
        return 1 if output > 0 else 0


class IdentityActivator(object):
    def forward(self, weighted_input):
        return weighted_input

    def backward(self, output):
        return 1

#y=1/(1+e^(-x)),y的导数是y*(1-y)
class SigmoidActivator(object):
    def forward(self, weighted_input):
        return 1.0 / (1.0 + np.exp(-weighted_input))

    def backward(self, output):
        return output * (1 - output)

#tanh=(e^x-e^-x)/(e^x+e^-x)
class TanhActivator(object):
    def forward(self, weighted_input):
        return 2.0 / (1.0 + np.exp(-2 * weighted_input)) - 1.0

    def backward(self, output):
        return 1 - output * output