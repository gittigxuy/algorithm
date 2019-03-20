# -*- coding:utf-8 -*- 
__author__ = 'xuy'

# -*- coding: UTF-8 -*-
import numpy as np
from activators import ReluActivator, IdentityActivator


# 获取图像中卷积区域
def get_patch(input_array, i, j, filter_width,
              filter_height, stride):
    '''
    从输入数组中获取本次卷积的区域，
    自动适配输入为2D和3D的情况
    '''
    start_i = i * stride
    start_j = j * stride
    #[height,width]
    if input_array.ndim == 2:
        return input_array[
               start_i: start_i + filter_height,
               start_j: start_j + filter_width]
    #[channel,height,width]
    elif input_array.ndim == 3:
        return input_array[:,
               start_i: start_i + filter_height,
               start_j: start_j + filter_width]


# 获取一个2D区域的最大值所在的索引
def get_max_index(array):
    max_i = 0
    max_j = 0
    max_value = array[0, 0]
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] > max_value:
                max_value = array[i, j]
                max_i, max_j = i, j
    return max_i, max_j


# 计算卷积
def conv(input_array,
         kernel_array,
         output_array,
         stride, bias):
    '''
    计算卷积，自动适配输入为2D和3D的情况
    '''
    channel_number = input_array.ndim
    output_height = output_array.shape[0]
    output_width = output_array.shape[1]


    #因为涉及到２Ｄ或者是3D的conv，因此只能用负数来获取kernel_width+kernel_height
    kernel_width = kernel_array.shape[-1]
    kernel_height = kernel_array.shape[-2]
    for i in range(output_height):#dim=0
        for j in range(output_width):#dim=1
            #对应元素相乘之后{get_patch*kernel_array}，再相加{get_patch*kernel_array}.sum(),最后加上bias
            #其中get_patch是获取图像中的卷积区域，kernel_array表示卷积核
            output_array[i][j] = (
                                     get_patch(input_array, i, j, kernel_width,
                                               kernel_height, stride) * kernel_array
                                 ).sum() + bias


# 为数组增加Zero padding
def padding(input_array, zp):
    '''
    为数组增加Zero padding，自动适配输入为2D和3D的情况
    '''
    if zp == 0:
        return input_array
    else:
        if input_array.ndim == 3:
            input_width = input_array.shape[2]
            input_height = input_array.shape[1]
            input_depth = input_array.shape[0]

            #创建padded_array的大小
            padded_array = np.zeros((
                input_depth,#channel
                input_height + 2 * zp,#height
                input_width + 2 * zp))
            #向里面赋值
            padded_array[:,
            zp: zp + input_height,
            zp: zp + input_width] = input_array
            return padded_array
        elif input_array.ndim == 2:
            input_width = input_array.shape[1]
            input_height = input_array.shape[0]
            # 创建padded_array的大小
            padded_array = np.zeros((
                input_height + 2 * zp,
                input_width + 2 * zp))
            # 向里面赋值
            padded_array[zp: zp + input_height,
            zp: zp + input_width] = input_array
            return padded_array


# 对numpy数组进行element wise操作,逐个操作,op表示激活函数
def element_wise_op(array, op):
    for i in np.nditer(array,
                       op_flags=['readwrite']):
        #对于每个output_array元素进行激活
        i[...] = op(i)

#卷积核的参数信息
class Filter(object):
    def __init__(self, width, height, depth):
        #随机初始化weights
        self.weights = np.random.uniform(-1e-4, 1e-4,
                                         (depth, height, width))
        self.bias = 0
        self.weights_grad = np.zeros(
            self.weights.shape)
        self.bias_grad = 0

    def __repr__(self):
        return 'filter weights:\n%s\nbias:\n%s' % (
            repr(self.weights), repr(self.bias))

    def get_weights(self):
        return self.weights

    def get_bias(self):
        return self.bias
    #采用梯度下降的方式更新权值
    def update(self, learning_rate):
        self.weights -= learning_rate * self.weights_grad
        self.bias -= learning_rate * self.bias_grad


class ConvLayer(object):
    def __init__(self, input_width, input_height,
                 channel_number, filter_width,
                 filter_height, filter_number,
                 zero_padding, stride, activator,
                 learning_rate):
        self.input_width = input_width
        self.input_height = input_height
        self.channel_number = channel_number
        self.filter_width = filter_width
        self.filter_height = filter_height
        self.filter_number = filter_number
        self.zero_padding = zero_padding
        self.stride = stride
        self.output_width = \
            ConvLayer.calculate_output_size(
                self.input_width, filter_width, zero_padding,
                stride)
        self.output_height = \
            ConvLayer.calculate_output_size(
                self.input_height, filter_height, zero_padding,
                stride)
        self.output_array = np.zeros((self.filter_number,
                                      self.output_height, self.output_width))
        self.filters = []
        for i in range(filter_number):
            self.filters.append(Filter(filter_width,
                                       filter_height, self.channel_number))
        self.activator = activator
        self.learning_rate = learning_rate
    #conv的前向传播
    def forward(self, input_array):
        '''
        计算卷积层的输出
        输出结果保存在self.output_array
        '''
        self.input_array = input_array
        #padded_input=input_array+padding
        self.padded_input_array = padding(input_array,
                                          self.zero_padding)
        """

        def conv(input_array,
         kernel_array,
         output_array,
         stride, bias):
         forward conv
        """

        """
        1)计算卷积，结果为output_array
        ２）对于output_array进行激活函数
        """
        for f in range(self.filter_number):
            filter = self.filters[f]
            #conv的输入：经过padding之后的input_array,+conv kernel
            conv(self.padded_input_array,
                 filter.get_weights(), self.output_array[f],
                 self.stride, filter.get_bias())
        element_wise_op(self.output_array,
                        self.activator.forward)

    def backward(self, input_array, sensitivity_array,
                 activator):
        '''
        １）计算传递给前一层的误差项,保存在self.delta_array
        ２）计算每个权重的梯度并且保存在Filter对象的weights_grad当中
        ３）update weight
        '''
        #在进行反向传播之前，先进行前向传播，然后计算上一层的｛误差＋梯度｝
        # 前向传播计算每个神经元a_i的输出值a_j

        self.forward(input_array)
        # １）计算传递给前一层的误差项, 保存在self.delta_array
        self.bp_sensitivity_map(sensitivity_array,
                                activator)
        # ２）计算每个权重的梯度并且保存在Filter对象的weights_grad当中
        self.bp_gradient(sensitivity_array)
    #3)调用filter类的update函数，update weight
    def update(self):
        '''
        按照梯度下降，更新权重
        '''
        for filter in self.filters:
            filter.update(self.learning_rate)
    #bp_step1:计算误差,传递到上一层的sensitivity map[敏感度/误差]

    #反向传播的上一层的误差项＝误差对于layer求偏导数＝（误差对于每一层的神经元求偏导数）×（每个神经元对layer求偏导数）＝（第一项＝w*当前层的误差）*（第二项＝每个神经元对layer求偏导数）
    #其中第一项在这里的具体实现是：１）添加zero padding 2)将filter【conv kernel】旋转１８０度
    def bp_sensitivity_map(self, sensitivity_array,
                           activator):
        '''
        step1:计算误差传递到上一层的sensitivity map
        sensitivity_array: 本层的sensitivity map
        activator: 上一层的激活函数
        '''
        # 处理卷积步长，对原始sensitivity map进行扩展,将stride=S还原为stride=1的sensitivity map
        expanded_array = self.expand_sensitivity_map(
            sensitivity_array)
        # full卷积，对sensitivitiy map进行zero padding
        # 虽然原始输入的zero padding单元也会获得残差
        # 但这个残差不需要继续向上传递，因此就不计算了
        expanded_width = expanded_array.shape[2]
        #添加zero padding
        zp = int((self.input_width +
                  self.filter_width - 1 - expanded_width) / 2)
        # 补一圈０
        padded_array = padding(expanded_array, zp)
        # 初始化delta_array，用于保存传递到上一层的,计算误差
        # sensitivity map，
        # 1)计算前一层的误差项
        self.delta_array = self.create_delta_array()
        # 对于具有多个filter的卷积层来说，最终传递到上一层的
        # sensitivity map相当于所有的filter的
        # sensitivity map之和
        for f in range(self.filter_number):
            filter = self.filters[f]
            # 将filter权重翻转180度，此时完成了对于误差对于当前层的神经元的求偏导数
            flipped_weights = np.array(list(map(
                lambda i: np.rot90(i, 2),
                filter.get_weights())))
            # 计算与一个filter对应的delta_array
            delta_array = self.create_delta_array()
            for d in range(delta_array.shape[0]):
                #conv(input_array,kernel_array,output_array,stride,bias)
                conv(padded_array[f], flipped_weights[d], delta_array[d], 1, 0)
            self.delta_array += delta_array
        # 将计算结果与激活函数的偏导数做element-wise乘法操作
        derivative_array = np.array(self.input_array)
        element_wise_op(derivative_array,
                        activator.backward)
        #误差的最终结果
        self.delta_array *= derivative_array
    # bp_step2:计算每个权重的梯度并且保存在Filter对象的weights_grad当中
    def bp_gradient(self, sensitivity_array):
        # 处理卷积步长，对原始sensitivity map进行扩展,将stride=S改为stride=1
        expanded_array = self.expand_sensitivity_map(
            sensitivity_array)

        """

                def conv(input_array,
                 kernel_array,
                 output_array,
                 stride, bias):
                 forward conv

    for f in range(self.filter_number):
        filter = self.filters[f]
        # conv的输入：经过padding之后的input_array,+conv kernel
        conv(self.padded_input_array,
             filter.get_weights(), self.output_array[f],
             self.stride, filter.get_bias())
        """

        for f in range(self.filter_number):
            # 计算每个权重的梯度
            filter = self.filters[f]
            for d in range(filter.weights.shape[0]):
                conv(self.padded_input_array[d],
                     expanded_array[f],#kernel_array
                     filter.weights_grad[d],#输出的是kernel的梯度
                     1,#反向传播的stride=1
                     0)
            # 计算偏置项的梯度
            filter.bias_grad = expanded_array[f].sum()

    #将原来stride=S，还原为stride=1
    def expand_sensitivity_map(self, sensitivity_array):
        depth = sensitivity_array.shape[0]
        # 确定扩展后sensitivity map的大小
        # 计算stride为1时sensitivity map的大小
        expanded_width = (self.input_width -
                          self.filter_width + 2 * self.zero_padding + 1)
        expanded_height = (self.input_height -
                           self.filter_height + 2 * self.zero_padding + 1)
        # 构建新的sensitivity_map
        expand_array = np.zeros((depth, expanded_height,
                                 expanded_width))
        # 从原始sensitivity map拷贝误差值
        for i in range(self.output_height):
            for j in range(self.output_width):
                i_pos = i * self.stride
                j_pos = j * self.stride
                expand_array[:, i_pos, j_pos] = \
                    sensitivity_array[:, i, j]
        return expand_array

    def create_delta_array(self):
        return np.zeros((self.channel_number,
                         self.input_height, self.input_width))

    @staticmethod
    def calculate_output_size(input_size,
                              filter_size, zero_padding, stride):
        return int((input_size - filter_size +
                    2 * zero_padding) / stride + 1)

# pooling并没有权重更新，因此在反向传播的过程中，向前传递误差，不传递梯度
class MaxPoolingLayer(object):
    def __init__(self, input_width, input_height,
                 channel_number, filter_width,
                 filter_height, stride):
        self.input_width = input_width
        self.input_height = input_height
        self.channel_number = channel_number
        self.filter_width = filter_width
        self.filter_height = filter_height
        self.stride = stride
        self.output_width = int((input_width -
                                 filter_width) / self.stride + 1)
        self.output_height = int((input_height -
                                  filter_height) / self.stride + 1)
        self.output_array = np.zeros((self.channel_number,
                                      self.output_height, self.output_width))

    def forward(self, input_array):
        for d in range(self.channel_number):
            for i in range(self.output_height):
                for j in range(self.output_width):
                    self.output_array[d, i, j] = (
                        get_patch(input_array[d], i, j,
                                  self.filter_width,
                                  self.filter_height,
                                  self.stride).max())

    def backward(self, input_array, sensitivity_array):
        self.delta_array = np.zeros(input_array.shape)
        for d in range(self.channel_number):
            for i in range(self.output_height):
                for j in range(self.output_width):
                    patch_array = get_patch(
                        input_array[d], i, j,
                        self.filter_width,
                        self.filter_height,
                        self.stride)
                    k, l = get_max_index(patch_array)
                    self.delta_array[d,
                                     i * self.stride + k,
                                     j * self.stride + l] = \
                        sensitivity_array[d, i, j]


def init_test():
    # channel=3*height=5*width=5
    a = np.array(
        [[[0, 1, 1, 0, 2],
          [2, 2, 2, 2, 1],
          [1, 0, 0, 2, 0],
          [0, 1, 1, 0, 0],
          [1, 2, 0, 0, 2]],
         [[1, 0, 2, 2, 0],
          [0, 0, 0, 2, 0],
          [1, 2, 1, 2, 1],
          [1, 0, 0, 0, 0],
          [1, 2, 1, 1, 1]],
         [[2, 1, 2, 0, 0],
          [1, 0, 0, 1, 0],
          [0, 2, 1, 0, 1],
          [0, 1, 2, 2, 2],
          [2, 1, 0, 0, 1]]])
    #3*3*3
    b = np.array(
        [[[0, 1, 1],
          [2, 2, 2],
          [1, 0, 0]],
         [[1, 0, 2],
          [0, 0, 0],
          [1, 2, 1]]])

    # def ConvLayer.__init__(self, input_width, input_height,
    #              channel_number, filter_width,
    #              filter_height, filter_number,
    #              zero_padding, stride, activator,
    #              learning_rate):
    cl = ConvLayer(5, 5, 3, 3, 3, 2, 1, 2, IdentityActivator(), 0.001)
    cl.filters[0].weights = np.array(
        [[[-1, 1, 0],
          [0, 1, 0],
          [0, 1, 1]],
         [[-1, -1, 0],
          [0, 0, 0],
          [0, -1, 0]],
         [[0, 0, -1],
          [0, 1, 0],
          [1, -1, -1]]], dtype=np.float64)
    cl.filters[0].bias = 1
    cl.filters[1].weights = np.array(
        [[[1, 1, -1],
          [-1, -1, 1],
          [0, -1, 1]],
         [[0, 1, 0],
          [-1, 0, -1],
          [-1, 1, 0]],
         [[-1, 0, 0],
          [-1, 0, 1],
          [-1, 0, 0]]], dtype=np.float64)
    return a, b, cl

# 前向传播的计算
def test():
    a, b, cl = init_test()
    cl.forward(a)
    print(cl.output_array)


def test_bp():
    a, b, cl = init_test()
    #完成计算误差　＋　计算梯度
    cl.backward(a, b, IdentityActivator())
    #更新权重参数
    cl.update()
    print(cl.filters[0])
    print(cl.filters[1])


def gradient_check():
    '''
    梯度检查
    '''
    # 设计一个误差函数，取所有节点输出项之和
    error_function = lambda o: o.sum()

    # 计算conv层的forward值，ｉｎｐｕｔ,kernel_size,conv layer
    a, b, cl = init_test()
    cl.forward(a)

    # 求取sensitivity map，表示前一层的误差
    sensitivity_array = np.ones(cl.output_array.shape,
                                dtype=np.float64)
    # 计算梯度，a表示input_array,在反向传播之前，先调用前向传播
    cl.backward(a, sensitivity_array,
                IdentityActivator())
    # 检查梯度
    epsilon = 10e-4
    for d in range(cl.filters[0].weights_grad.shape[0]):
        for i in range(cl.filters[0].weights_grad.shape[1]):
            for j in range(cl.filters[0].weights_grad.shape[2]):
                cl.filters[0].weights[d, i, j] += epsilon
                cl.forward(a)
                # 取所有节点输出项之和
                err1 = error_function(cl.output_array)
                cl.filters[0].weights[d, i, j] -= 2 * epsilon
                cl.forward(a)
                err2 = error_function(cl.output_array)
                expect_grad = int((err1 - err2) / (2 * epsilon))
                cl.filters[0].weights[d, i, j] += epsilon
                print('weights(%d,%d,%d): expected - actural %f - %f' % (
                    d, i, j, expect_grad, cl.filters[0].weights_grad[d, i, j]))


def init_pool_test():
    a = np.array(
        [[[1, 1, 2, 4],
          [5, 6, 7, 8],
          [3, 2, 1, 0],
          [1, 2, 3, 4]],
         [[0, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 0, 1],
          [3, 4, 5, 6]]], dtype=np.float64)

    b = np.array(
        [[[1, 2],
          [2, 4]],
         [[3, 5],
          [8, 2]]], dtype=np.float64)

    mpl = MaxPoolingLayer(4, 4, 2, 2, 2, 2)

    return a, b, mpl


def test_pool():
    a, b, mpl = init_pool_test()
    mpl.forward(a)
    print('input array:\n%s\noutput array:\n%s' % (a,
                                                   mpl.output_array))


def test_pool_bp():
    a, b, mpl = init_pool_test()
    mpl.backward(a, b)
    print('input array:\n%s\nsensitivity array:\n%s\ndelta array:\n%s' % (
        a, b, mpl.delta_array))