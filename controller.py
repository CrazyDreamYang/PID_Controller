# -*-coding:utf-8 -*-
# Author :Yang
# Data:2021/10/22 15:47
import matplotlib.pyplot as plt

#增量式PID系统
class IncrementalPID:
    def __init__(self, P:float ,I:float ,D:float ):
        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.PIDOutput =0.0         #PID控制器输出
        self.SystemOutput = 0.0     #系统输出值
        self.LastSystemOutput = 0.0 #系统的上一次输出

        self.Error = 0.0
        self.LastError = 0.0
        self.LastLastError = 0.0

    #设置PID控制器参数
    def SetStepSignal(self,StepSignal):
        self.Error = StepSignal - self.SystemOutput
        #计算增量
        IncrementalValue = self.Kp*(self.Error - self.LastError)\
            + self.Ki * self.Error +self.Kd *(self.Error -2*self.LastError +self.LastLastError)
        #计算输出
        self.PIDOutput += IncrementalValue
        self.LastLastError = self.LastError
        self.LastError = self.Error

    #以一阶惯性环节为例子演示控制效果
    def SetInertiaTime(self,IntertiaTime,SampleTime):
        self.SystemOutput = (IntertiaTime*self.LastSystemOutput + SampleTime *self.PIDOutput)/(SampleTime + IntertiaTime)
        self.LastSystemOutput = self.SystemOutput


#位置式PID系统
class PositionalPID:
    def __init__(self, P: float, I: float, D: float):
        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.PIDOutput = 0.0  # PID控制器输出
        self.SystemOutput = 0.0  # 系统输出值
        self.LastSystemOutput = 0.0  # 系统的上一次输出

        self.PIDErrAdd = 0.0
        self.ResultValueBack = 0.0
        self.Error = 0.0
        self.LastError = 0.0

    def SetStepSignal(self, StepSignal):
        self.Error = StepSignal - self.SystemOutput

        KpWork  =self.Kp *self.Error
        KiWork = self.Ki* self.PIDErrAdd
        KdWork = self.Kd * (self.Error- self.LastError)
        self.PIDOutput = KpWork + KiWork + KdWork
        self.PIDErrAdd += self.Error
        self.LastError = self.Error

        # 以一阶惯性环节为例子演示控制效果

    def SetInertiaTime(self, IntertiaTime, SampleTime):
        self.SystemOutput = (IntertiaTime * self.LastSystemOutput + SampleTime * self.PIDOutput) / (
                    SampleTime + IntertiaTime)
        self.LastSystemOutput = self.SystemOutput


class Withoutcontorller:
   def __init__(self, StepSignal:float):
       self.SystemOutput = 0.0
       self.LastSystemOutput = 0
       self. StepSignal =  StepSignal

   def SetInertiaTime(self, IntertiaTime, SampleTime):
       self.SystemOutput = (IntertiaTime * self.LastSystemOutput + SampleTime * self.StepSignal) / (
                    SampleTime + IntertiaTime)
       self.LastSystemOutput = self.SystemOutput




