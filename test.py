# -*-coding:utf-8 -*-
# Author :Yang
# Data:2021/10/22 18:21
import matplotlib.pyplot as plt
from controller import IncrementalPID,PositionalPID,Withoutcontorller

#测试PID程序

def TestPID(P:float ,I:float ,D:float ,StepSingal:float):
    IncrementalPid =  IncrementalPID(P, I , D)
    Positionalpid = PositionalPID(P, I , D)
    Withoutcontorl = Withoutcontorller(StepSingal)
    #IncrementalXaxis = [0]
    IncrementalYaxis = [0]
    Xaxis = [0]
    PositionalYaxis = [0]
    WithoutcontorlYaxis = [0]

    StepSingalaxis = [StepSingal]

    for i in range(1,500):
        #增量式
        IncrementalPid.SetStepSignal(StepSingal)#设置参考信号
        IncrementalPid.SetInertiaTime(3, 0.1)#设置常数
        IncrementalYaxis.append(IncrementalPid.SystemOutput)
        #IncrementalXaxis.append(i)

        #位置式
        Positionalpid.SetStepSignal(StepSingal)
        Positionalpid.SetInertiaTime(3, 0.1)
        PositionalYaxis.append(Positionalpid.SystemOutput)

        #无控制器
        Withoutcontorl.SetInertiaTime(3, 0.1)
        WithoutcontorlYaxis.append(Withoutcontorl.SystemOutput)

        StepSingalaxis.append(StepSingal)
        Xaxis.append(i)

    plt.figure(1)
    plt.plot(Xaxis, IncrementalYaxis,label='IncrementalPid',color ='r')
    plt.plot(Xaxis, PositionalYaxis, label='PositionalPid',color ='b')
    plt.plot(Xaxis, WithoutcontorlYaxis, label='Withoutcontorl', color='black')
    plt.plot(Xaxis, StepSingalaxis, dashes=[6, 2],label= 'SetSignal',color ='g')

    plt.xlim(0,120)
    plt.ylim(0,140)
    plt.xlabel('t')
    plt.ylabel('output')
    plt.title("PidContorller")

    # plt.figure(2)
    # plt.xlim(0, 120)
    # plt.ylim(0, 140)
    # plt.title("PositionalPid")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    TestPID(5.0,0.5,0.1,100.0)


