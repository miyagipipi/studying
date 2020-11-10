# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:47:48 2020

@author: LQS
"""
#先按正态分布随机出一个数作平均数，再给一个随机正态分布数字作方差
#给出的平均数要判断区间，不能太大也不能太小，同理方差也要判断边界
#按这两个数带入正态分布的平均数和方差中，得出一组3个数值，也要判断边界
import random

mean = float(input('平均值: '))
div = float(input('方差: '))
nums = 3 * float(input('几组: '))
_max = float(input('最大值: '))
_min = float(input('最小值: '))

with open(r'D:\金属硬度\正态分布数据.txt','a') as f:
    i = 1
    while i <= nums:
        v = round(random.normalvariate(mean, div), 1)
        if v < _min: v = _min
        elif v >= _max: v = _max
        if i % 3 == 0:
            f.write(str(v) + '\n')
            
        else:
            f.write(str(v) + '\t')
        i += 1
print('When inputting data into excel, please delete these data for next using!')

class metalHardness(object):
    