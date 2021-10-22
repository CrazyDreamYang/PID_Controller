# PID_contrller
## 一、简介
这个项目中，采用python编写了位置式PID与增量式PID这两种控制器的程序，被控系统选择了一阶惯性系统。控制效果如下图。


![image](https://user-images.githubusercontent.com/53599513/138470269-bc198261-7b8d-41e4-92eb-3c66804646f9.png)



- 有关控制器的介绍，请访问[链接](https://blog.csdn.net/qq_43571752/article/details/120895749)
## 文件结构
- controller.py 中添加了三个类，用来分别是位置式PID控制系统、增量式PID控制系统与无控制器的一阶惯性系统。
- test.py 用来测试控制系统及绘图。
