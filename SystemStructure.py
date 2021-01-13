'''
Power System Analysis
Author: 梁飞，单士磊，蒋奕琛
Date: 2021.1.13
本程序仅用于课堂展示
'''

import numpy as np
from math import *


class Line:
    '''
    self.r: 电阻，阻抗的实数部分，单位是欧姆
    self.x: 电抗，阻抗的虚数部分，单位是欧姆
    self.g: 电导，导纳的实数部分，单位是西门子（S）
    self.b: 电纳，导纳的虚数部分，单位是西门子（S）
    '''
    def __init__(self, lineType='LGJ-300/50', distance=20.0, req=100.0, n=1, length=200.0,
                 paraKnown=False, paras=(0.0, 0.0, 0.0, 0.0)):
        '''
        初始化传输线，计算R, X, B, G
        :param lineType: 传输线类型
        :param distance: 传输线间几何平均距离(mm)
        :param req: 等效半径(mm)
        :param n: 传输线分割数
        :param length: 传输线长度(km)
        '''
        self.lineType = ''
        self.distance = 0.
        self.req = 0.
        self.n = 1
        self.length = 0.
        self.paraKnown = paraKnown
        if paraKnown:
            # 如果已知传输线R, X, B, G则省去计算步骤
            self.r = paras[0]
            self.x = paras[1]
            self.b = paras[2]
            self.g = paras[3]
        else:
            self.lineType = lineType
            self.distance = distance
            self.req = req
            self.n = n
            self.length = length

            # 计算R, X, B, G
            type = lineType.split('-')[0]
            area = float(lineType.split('-')[1].split('/')[0])

            if isinstance(distance, (list, tuple)):
                n0 = len(distance)
                distance = pow(np.prod(distance), 1 / n0)
                # print(distance)
            distance = distance*1000
            if length <= 300:
                if type == 'LGJ':
                    r1 = 31.5 / (n * area)
                if type == 'LGJ':
                    # 需要补充其他导线类型
                    pass
                x1 = 0.1445 * log10(distance / req) + 0.0157 / n
                b1 = 7.58 / (log10(distance / req)) * 10**(-6)
                self.r = r1 * length
                self.x = x1 * length
                self.b = b1 * length
                self.g = 0
            if length > 300:
                if type == 'LGJ':
                    r1 = 31.5 / (n * area)
                if type == 'LGJ':
                    # 需要补充其他导线类型
                    pass
                x1 = 0.1445 * log10(distance / req) + 0.0157 / n
                b1 = 7.58 / (log10(distance / req)) * 10**(-6)
                kr = 1 - x1 * b1 * length**2 / 3
                kx = 1 - (x1 * b1 - r1**2 * b1 / x1) * length**2 / 6
                kb = 1 + x1 * b1 * length**2 / 12
                self.r = r1 * length
                self.x = x1 * length
                self.b = b1 * length

                self.r = kr * self.r
                self.x = kx * self.x
                self.b = kb * self.b
                self.g = 0

    @property
    def R(self):
        '''
        :return: 电阻 R value
        '''
        return self.r

    @property
    def X(self):
        '''
        :return: 电抗X value
        '''
        return self.x

    @property
    def B(self):
        '''
        :return: 电纳B value
        '''
        return self.b

    @property
    def G(self):
        '''
        :return: 电导G value
        '''
        return self.g

    def get_paras(self):
        '''
        返回传输线的四个参数
        :return: tuple (R, X, B, G)
        '''
        return self.r, self.x, self.b, self.g


class Transformer:
    def __init__(self, Pk=500.0, Uk=5.0, Un=220.0, Po=100.0, Io=2.0, ratio=(231, 121), Sn=400.0,
                 paraKnown=False, paras=(0.0, 0.0, 0.0, 0.0)):
        '''
        初始化变压器，计算R, X, B, G
        :param Pk: 短路功率(kW)
        :param Uk: Uk%， 短路电压比
        :param Un: 额定电压(kV)
        :param P0: 开路功率(kW)
        :param I0: 开路电流比
        :param ratio: 电压比
        :param Sn: 视在功率(MVA)
        '''
        self.Pk = 0.
        self.Uk = 0.
        self.Un = 0.
        self.Po = 0.
        self.Io = 0.
        self.ratio = (0., 0.)
        self.Sn = 0.
        self.paraKnown = paraKnown
        if paraKnown is True:
            self.ratio = ratio
            self.r = paras[0]
            self.x = paras[1]
            self.b = paras[2]
            self.g = paras[3]
        else:
            # 变压器参数均为复变一侧计算值
            self.Pk = Pk
            self.Uk = Uk
            self.Un = Un
            self.Po = Po
            self.Io = Io
            self.ratio = ratio
            k = self.ratio[0] / self.ratio[1]
            self.Sn = Sn
            self.r = Pk * Un**2 / (1000 * Sn**2)
            self.x = Uk * Un**2 / (100 * Sn)
            self.b = Po / (1000 * Un**2)
            self.g = Io * Sn / (100 * Un**2)

            # self.r = Pk * Un**2 / (1000 * Sn**2)
            # self.x = Uk * Un**2 / (100 * Sn)
            # self.b = Po / (1000 * Un**2)
            # self.g = Io / (100 * Un**2)

    @property
    def R(self):
        return self.r

    @property
    def X(self):
        return self.x

    @property
    def B(self):
        return self.b

    @property
    def G(self):
        return self.g

    def get_paras(self):
        return self.R, self.X, self.B, self.G


class PowerGrid:
    def __init__(self):
        self.adm_matrix = [[]]  # Admittance matrix
        self.V_initial = False  # 是否设置V-theta结点
        self.numBus = 0  # 节点的数目
        self.numBus1 = 0  # PQ结点的数目
        self.numBus2 = 0  # PV结点的数目
        self.char_matrix = []  # [bus type, e, f, P, Q, V, k]
        # bus type: bus的类型
        # e:电压的实数部分，单位是V
        # f:电压的虚数部分，单位是V
        # P：功率的实数部分，单位是MW
        # Q：功率的虚数部分，单位是Mvar
        # V：PV节点的电压值，单位是KV
        # k: 电压等级与标准之比
        self.numLine = 0
        self.numTransformer = 0
        self.line_list = []
        self.transformer_list = []
        self.result = []
        self.loss_list = []

    def get_adm_matrix(self):
        '''
        计算admittance matrix
        '''
        if sum(map(sum, self.adm_matrix)) != 0:
            return self.adm_matrix
        device_list = self.line_list + self.transformer_list
        for location, device in device_list:
            k, l = location
            if type(device) == Line:
                level = self.char_matrix[k][6]
                # 在k，k的位置放上R+Xj的倒数，以及两个节点之间的B的一半
                self.adm_matrix[k][k] += 1 / (level * level * complex(device.R, device.X)) \
                                         + complex(0, device.B / 2) / (level * level)
                # 在l，l的位置上放上R+Xj的倒数
                self.adm_matrix[l][l] += 1 / (level * level * complex(device.R, device.X)) \
                                         + complex(0, device.B / 2) / (level * level)
                # 这两行是在（k，l）和（l，k）的位置上放上相应的Y_kl和Y_lk的值，Y_kl = Y_lk = -1/(R+Xj)
                self.adm_matrix[l][k] = -1 / (level * level * complex(device.R, device.X))
                self.adm_matrix[k][l] = -1 / (level * level * complex(device.R, device.X))
            if type(device) == Transformer:
                level_k = self.char_matrix[k][6]
                level_l = self.char_matrix[k][6]
                # 在k，k的位置放上R+Xj的倒数，以及两个节点之间的B的一半
                self.adm_matrix[k][k] += 1 / (level_k * level_k * complex(device.R, device.X)) \
                                         + complex(device.G, device.B) / (level_k * level_k)
                # 在l，l的位置上放上R+Xj的倒数
                self.adm_matrix[l][l] += 1 / (level_k * level_k * complex(device.R, device.X))
                # 这两行是在（k，l）和（l，k）的位置上放上相应的Y_kl和Y_lk的值，Y_kl = Y_lk = -1/(R+Xj)
                self.adm_matrix[l][k] = -1 / (level_k * level_k * complex(device.R, device.X))
                self.adm_matrix[k][l] = -1 / (level_k * level_k * complex(device.R, device.X))
        return self.adm_matrix

    def print_grid(self):
        print("Bus总数：{}".format(self.numBus))
        print("PQ-bus总数：{}".format(self.numBus1))
        print("PV-bus总数：{}".format(self.numBus2))
        print("Admittance matrix: ")
        for row in self.adm_matrix:
            print(row)
        print('Characteristic matrix: ')
        print('bus type | e | f | P | Q | V | k')
        for row in self.char_matrix:
            print(row)
        print('Result: ')
        print('bus type | e | f | P | Q | V | k')
        for row in self.result:
            print(row)

    def set_V(self, V=220.0, theta=0.0):
        '''
        设置V-theta bus
        :param V: 电压幅值(kV)
        :param theta: 电压幅角(rads)
        :return:
        '''
        if self.V_initial is False:
            self.adm_matrix[0].append(0.0)
            self.char_matrix.insert(0, [0, V * cos(theta), V * sin(theta), 0.0, 0.0, V, 1.0])
            self.numBus += 1
            self.V_initial = True
        else:
            self.char_matrix[0] = [0, V * cos(theta), V * sin(theta), 0.0, 0.0, V, 1.0]

    def add_bus(self, seq=-1, P=0.0, Q=0.0, V=0.0, k=1.0, busType=1):
        '''
        在电网中添加bus
        :param seq: bus的序号
        :param P: bus的有功(MW)
        :param Q: bus的无功(Mvar)
        :param V: bus的电压绝对值(kV)
        :param busType: bus的类型， 1：PQ bus, 2: PV bus
        :return:
        '''
        if self.V_initial is False:
            print("V-theta need to be set first before adding any other buses.")
            raise IndexError('V-theta need to be set first before adding any other buses.')

        # 初始化admittance matrix，所有的值设置成0.0
        for i in range(self.numBus):
            self.adm_matrix[i].append(0.0)
        self.adm_matrix.append([0.0] * (self.numBus + 1))

        # 更新PQ bus和PV bus的数量，char_matrix
        self.numBus += 1
        if seq == -1:
            self.char_matrix.append([busType, 0, 0, P, Q, V, k])
        else:
            self.char_matrix.insert(seq, [busType, 0, 0, P, Q, V, k])
        if busType == 1:
            self.numBus1 += 1
        if busType == 2:
            self.numBus2 += 1

    def delete_bus(self, seq=-1):
        '''
        删除结点
        :return:
        '''
        if self.numBus <= 1:
            # 如果没有PQ和PV结点的话，就报错
            print('No bus to delete!')
            raise ValueError
        else:
            # 删除admittance matrix 的最后一行和最后一列
            for i in range(self.numBus):
                self.adm_matrix[i].pop()
            self.adm_matrix.pop()
        self.numBus -= 1
        temp_bus = self.char_matrix.pop(seq)  # 删除char_matrix 的最后一行，并把矩阵赋给temp_matrix
        if temp_bus[0] == 1:
            self.numBus1 -= 1
            # 如果是PQbus的话，PQbus的数量减1
        if temp_bus[0] == 2:
            self.numBus2 -= 1

    def add_line(self, location, device, seq=-1):
        '''
        在系统里面添加传输线
        :param location: 线在哪两个结点之间，格式tuple(l,k)
        :param device: Line type
        :return:
        '''
        if seq == -1:
            self.line_list.append((location, device))
        else:
            self.line_list.insert(seq, (location, device))
        self.numLine += 1

    def add_transformer(self, location, device, seq=-1):
        '''
        在系统里面添加变压器
        :param location: 变压器在哪两个结点之间，格式tuple(l,k)
        :param device: Line type
        :return:
        '''
        if seq == -1:
            self.transformer_list.append((location, device))
        else:
            self.transformer_list.insert(seq, (location, device))
        self.numTransformer += 1

    def delete_line(self, seq=-1):
        # 从系统里面删除传输线
        self.line_list.pop(seq)
        self.numLine -= 1

    def delete_transformer(self, seq=-1):
        #从系统里面删除变压器
        self.transformer_list.pop(seq)
        self.numTransformer -= 1

    def calculate_V(self, maxIter, xTol):
        '''
        计算V
        :param maxIter: 最大迭代次数
        :param xTol: 最大误差
        :return:
        '''
        if self.V_initial is False:
            raise ValueError('Voltage need to be set before calculate.')

        iter = 0  # 迭代次数计数器
        n1 = self.numBus1
        n2 = self.numBus2
        n = self.numBus
        M = np.array(self.char_matrix)
        e = [self.char_matrix[0][1]] * n
        e = np.array(e).reshape(-1, 1)
        # e = M[:, 1].reshape(-1, 1)
        f = M[:, 2].reshape(-1, 1)
        Y = np.array(self.adm_matrix)
        P = M[:, 3].reshape(-1, 1)
        Q = M[:, 4].reshape(-1, 1)
        V = M[:, 5].reshape(-1, 1)
        k = M[:, 6].reshape(-1, 1)
        V = V * k

        while iter < maxIter:
            diff_F = dF(Y, P, Q, V, e, f, n1, n2)  # 函数，F的变化量
            J = Jacobi(Y, e, f, n1, n2)
            diff_x = np.linalg.inv(J).dot(diff_F)  # 求x的变化量， dx = J^{-1} * dF
            err = np.linalg.norm(diff_x, ord=2, axis=None, keepdims=False)  # 求误差的模
            if err < xTol:
                break
            e[1:, ] += diff_x[n-1:, ]  # 迭代e
            f[1:, ] += diff_x[:n-1, ]  # 迭代f
            iter += 1

        # 检查！！
        e = e / k
        f = f / k

        M[:, 1] = e.reshape(1, -1)
        M[:, 2] = f.reshape(1, -1)

        self.result = M.tolist()
        for i in range(self.numBus):
            self.result[i][0] = int(self.result[i][0])

        self.loss_list = []
        for line in self.line_list:
            l, k = line[0]
            loss = -((self.result[l][1] - self.result[k][1]) ** 2 +
                     (self.result[l][2] - self.result[k][2]) ** 2) * self.adm_matrix[l][k].conjugate()
            self.loss_list.append([(l, k), loss])

        for transformer in self.transformer_list:
            l, k = transformer[0]
            ratio = transformer[1].ratio[0] / transformer[1].ratio[1]
            loss = -((self.result[l][1] - ratio * self.result[k][1]) ** 2 +
                     (self.result[l][2] - ratio * self.result[k][2]) ** 2) * self.adm_matrix[l][k].conjugate()
            self.loss_list.append([(l, k), loss])

        #线流
        self.flow_list = []
        for line in self.line_list:
            l, k = line[0]
            flow = -(complex((self.result[l][1] - self.result[k][1]),
                      -(self.result[l][2] - self.result[k][2])) )*complex(self.result[l][1],self.result[l][2]) * self.adm_matrix[l][k].conjugate()
            self.flow_list.append([(l, k), flow])

        for transformer in self.transformer_list:
            l, k = transformer[0]
            ratio = self.char_matrix[k][6] / self.char_matrix[l][6]
            flow = -(complex((self.result[l][1] - ratio*self.result[k][1]),
                      -(self.result[l][2] - ratio*self.result[k][2])) )*complex(self.result[l][1],self.result[l][2]) * self.adm_matrix[l][k].conjugate()
            self.flow_list.append([(l, k), flow])



def Jacobi(Y, e, f, n1, n2):
    '''
    计算雅各比矩阵，并且要求输入可以用上面的代码计算出来的结果和形式
    :param Y: admittance matrix，单位是西门子S，复数， 类型2-d list, size n x n
    :param e: 需要求出的U=e+fj的实数部分，实数，单位是V，类型list, size n
    :param f: 需要求出的U=e+fj的虚数部分，实数，单位是V，类型list, size n
    :return: 雅各比矩阵 J size (2n-2) x (2n-2)
    '''
    U = np.zeros(len(e), dtype=complex)
    for i in range(len(e)):
        U[i] = complex(e[i], f[i])
    Ibus = Y.dot(U)

    J1 = np.diag(U).dot((Y.conj())) + np.diag(Ibus.conj())
    # H,J
    J2 = 1j * (np.conj(np.diag(Ibus)) - np.conj(Y).dot(np.diag(U)))

    J3 = np.diag(2 * U)

    L = len(J1) - 1
    J = np.zeros((L * 2, L * 2))
    # K = np.zeros((L * 2, L * 2))

    J[0:L, 0:L] = J2[1:, 1:].real
    J[0:L, L:] = J1[1:, 1:].real
    J[L: L+n1, 0:L] = J2[1:n1+1, 1:].imag
    J[L: L+n1, L:] = J1[1:n1+1, 1:].imag
    J[L+n1: L+n1+n2, 0:L] = J3[n1+1:, 1:].imag
    J[L+n1: L+n1+n2, L:] = J3[n1+1:, 1:].real

    # # original code, need to be justified
    # K[0::2, 1::2] = J1[1:, 1:].real
    # K[::2, ::2] = J2[1:, 1:].real
    # K[1::2, 1::2] = J1[1:, 1:].imag
    # K[1::2, ::2] = J2[1:, 1:].imag

    return J


def dF(Y, P, Q, V, e, f, n1, n2):
    '''
    求F的变化量
    :param Y: admittance matrix, size n x n
    :param P: active matrix , size n x 1
    :param Q: reactive matrix, size n x 1
    :param V: voltage matrix, size n x 1
    :param e: real part of voltage, size n x 1
    :param f: imaginary part of voltage , size n x 1
    :param n1: PQ结点的个数
    :param n2: PV结点的个数
    :return:
    '''
    G = Y.real
    B = Y.imag

    temp1 = np.dot(G, e) - np.dot(B, f)
    temp2 = np.dot(G, f) + np.dot(B, e)

    dP = P - (e * temp1 + f * temp2)
    dQ = Q - (f * temp1 - e * temp2)
    V2 = np.power(V, 2)
    dV2 = V2 - (np.power(e, 2) + np.power(f, 2))

    dF = np.concatenate((dP[1:, :], dQ[1:n1+1, :]), axis=0)
    dF = np.concatenate((dF, dV2[n1+1:n1+n2+1, :]), axis=0)
    return dF


def test():
    Transformer1 = Transformer(120, 10, 220, 60, 1, (220, 121), 120)
    print(Transformer1.get_paras())
    line1 = Line(distance=(1, 2, 4), req=69.66, n=2)
    print(line1.get_paras())

    powergrid1 = PowerGrid()

    powergrid1.set_V(1.06, 0)
    powergrid1.add_bus(P=0.2, Q=0.2, busType=1)
    powergrid1.add_bus(P=-0.45, Q=-0.15, busType=1)
    powergrid1.print_grid()

    powergrid1.delete_bus()
    powergrid1.print_grid()

    powergrid1.add_bus(P=-0.45, Q=-0.15, busType=1)
    powergrid1.add_bus(P=-0.4, Q=-0.05, busType=1)
    powergrid1.add_bus(P=-0.6, Q=-0.1, busType=1)
    powergrid1.add_line((0, 1), Line(paraKnown=True, paras=(0.02, 0.06, 0.0, 0.0)))
    powergrid1.add_line((0, 2), Line(paraKnown=True, paras=(0.08, 0.24, 0.0, 0.0)))
    powergrid1.add_line((1, 2), Line(paraKnown=True, paras=(0.06, 0.18, 0.0, 0.0)))
    powergrid1.add_line((1, 3), Line(paraKnown=True, paras=(0.06, 0.18, 0.0, 0.0)))
    powergrid1.add_line((1, 4), Line(paraKnown=True, paras=(0.04, 0.12, 0.0, 0.0)))
    powergrid1.add_line((2, 3), Line(paraKnown=True, paras=(0.01, 0.03, 0.0, 0.0)))
    powergrid1.add_line((3, 4), Line(paraKnown=True, paras=(0.08, 0.24, 0.0, 0.0)))

    powergrid1.get_adm_matrix()
    powergrid1.print_grid()

    M = np.array(powergrid1.char_matrix)
    e = M[:, 1].reshape(-1, 1)
    f = M[:, 2].reshape(-1, 1)
    Y = np.array(powergrid1.adm_matrix)
    P = M[:, 3].reshape(-1, 1)
    Q = M[:, 4].reshape(-1, 1)
    V = M[:, 5].reshape(-1, 1)
    np.set_printoptions(precision=3, suppress=True)
    print('Jacobi:')
    print(Jacobi(Y, e, f, powergrid1.numBus1, powergrid1.numBus2))
    print('dF:')
    print(dF(Y, P, Q, V, e, f, powergrid1.numBus1, powergrid1.numBus2))
    powergrid1.calculate_V(10, 1e-6)
    powergrid1.print_grid()


def test2():
    powergrid1 = PowerGrid()
    powergrid1.set_V(242)
    powergrid1.add_bus(busType=1, P=0, Q=20, k=1)
    powergrid1.add_bus(busType=1, P=-80, Q=-100, k=2)
    powergrid1.add_bus(busType=1, P=-50, Q=-50, k=2)
    powergrid1.add_bus(busType=1, P=-30, Q=20, k=1)

    powergrid1.add_line((0, 1), Line(distance=(15, 15, 30), req=12.13, n=1, length=200))
    powergrid1.add_line((0, 4), Line(distance=(15, 15, 30), req=12.13, n=1, length=200))
    powergrid1.add_line((2, 3), Line(distance=(15, 15, 30), req=12.13, n=1, length=250))
    powergrid1.add_transformer((1, 2), Transformer(Pk=500, Uk=5, Po=100, Io=2, ratio=(231, 121), Sn=400))
    powergrid1.add_transformer((4, 3), Transformer(Pk=500, Uk=5, Po=100, Io=2, ratio=(231, 110), Sn=400))

    powergrid1.get_adm_matrix()
    powergrid1.calculate_V(100, 1e-6)
    powergrid1.print_grid()


def test3():
    powergrid1 = PowerGrid()
    powergrid1.set_V(242)
    powergrid1.add_bus(busType=1, P=0, Q=10, k=1)
    powergrid1.add_bus(busType=1, P=-180, Q=-100, k=2)
    powergrid1.add_bus(busType=1, P=-50, Q=-30, k=2)
    powergrid1.add_bus(busType=1, P=40, Q=30, k=2)

    powergrid1.add_line((0, 1), Line(paraKnown=True, paras=(5.9, 31.5, 0.0, 0.0)))
    powergrid1.add_line((2, 3), Line(paraKnown=True, paras=(65, 100, 0.0, 0.0)))
    powergrid1.add_line((3, 4), Line(paraKnown=True, paras=(65, 100, 0.0, 0.0)))

    powergrid1.add_transformer((1, 2), Transformer(paraKnown=True, paras=(0.8, 23, 0.0, 0.0), ratio=(231, 121)))
    powergrid1.add_transformer((4, 3), Transformer(paraKnown=True, paras=(3, 110, 0.0, 0.0), ratio=(231, 110)))

    powergrid1.get_adm_matrix()
    powergrid1.calculate_V(100, 1e-6)
    powergrid1.print_grid()


if __name__ == '__main__':
    test2()
