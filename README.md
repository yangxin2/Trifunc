# Trifunc
# 可行性分析：

## 1. 引言

### 1.1 编写目的

该软件项目可行性研究分析是对三角函数计算器的全面通盘考虑，是项目分析员进行进一步工作的前提，是软件开发人员正确成功地开发项目的前提与基础。此分析可以使软件开发团体尽可能早地估计研制课题的可行性，可以在定义阶段较早地认识到系统方案的缺陷，从而节省时间、精力和资金，并且避免许多专业方面的困难。

### 1.2 背景

计算器是日常生活中十分便捷有效的工具，现在市面上的计算器种类丰富，功能齐全，覆盖多种设备，在交互模式上也形态各异，但整体的计算质量差异较大。

### 1.3 定义

实现简单快捷正确的三角函数计算的设备。

### 1.4 参考资料

[1]张海藩．软件工程导论（第五版）[M]．北京：清华大学出版社，2008

[2]金尊和．软件工程实践导论：有关方法、设计、实现、管理之三十六计[M]．北京：清华大学出版社，2005

[3]微软亚洲研究院．软件开发的科学与艺术[M]．青岛：电子工业出版社，2002

[4]R S. Pressman．软件工程—实践者的研究方法[M]．北京：机械工业出版社，2011

[5]周之英．现代软件工程[M]．北京：科学出版社，2000

## 2. 立项依据

### 2.1 项目背景

项目名称：三角函数计算器

项目提出者：重庆大学

项目开发者：重庆大学现代软件工程第五组

用户：需要计算三角函数的人群

### 2.2 项目开发的目的与意义

实现更友好的系统与用户之间的交互关系，提供准确的计算质量。

### 2.3 本团队开发条件概况

设备：团队拥有多台计算机及多个服务器，满足软件开发需求。

人员：杨欣：具有计算机相关比赛经历，知识体系完善。

      卢静雯：具有计算机相关比赛经历，知识体系完善。
      
      钟轶伟：具有计算机相关比赛经历，知识体系完善。
      
      刘子钰：具有计算机相关比赛经历，知识体系完善。
      
      胡榜涛：具有计算机相关比赛经历，知识体系完善。
      
## 3. 立项依据

### 3.1 项目开发的主要内容

1）计算功能的底层研发

2）人机交互界面显示

### 3.2 项目的预期目标

友好的系统与用户之间的交互关系，准确的计算质量。

### 3.3 项目开发分工

![image](https://github.com/yangxin2/Trifunc/blob/master/%E5%B0%8F%E7%BB%84%E5%88%86%E5%B7%A5.jpg)

### 3.4 项目开发计划

![image](https://github.com/yangxin2/Trifunc/blob/master/%E9%A1%B9%E7%9B%AE%E5%BC%80%E5%8F%91%E8%AE%A1%E5%88%92.jpg)

### 3.5 项目可行性分析结论

根据上述分析，该项目具有可行性。

# 需求分析：

## 1.引言

### 1.1 编写目的

在程序设计中，通过设计、编制、调试一个模拟计算器的程序，加深对语法及语义分析原理的理解，并实现对命令语句的灵活应用。在程序设计中，可以用两种方法解决问题：一是传统的结构化程序设计方法，二是更先进的面向对象程序设计方法。而在面向对象程序设计中关键是如何将问题域中的实体抽取出来，作为程序中的类，而属性与行为作为类的两类要素通常是必不可少的，甚至还应考虑类必须满足的约束。

### 1.2 项目背景

计算器的使用能够大大降低数学计算的难度，并提高计算的准确性和精确度，该计算器的使用非常简单和方便，对广大中小学生的学习有巨大帮助作用。

## 2.任务概述

### 2.1目标

设计的计算器软件满足友好的交互形式，提供准确的计算。

### 2.2 运行环境

系统开发平台为Pycharm，程序设计语言采用Python。

可以在Windows10、Ubuntu16.04运行。 

### 2.3 功能需求

实现简单三角函数计算的功能，要程序能够时间：sin、cos、arcsin、arctan四个运算功能；还要实现数据的输入、输出、计算、显示及程序退出等功能。

### 2.4 性能需求

精度：输入输出的精度都保持小数点后16位的精度

时间：计算过程的时间不超过300ms

### 2.5 输入输出要求

输入：角度制/弧度制/数字和计算式

输出：数值/角度制/弧度制

# 概要分析：

## 1.界面显示设计

![image](https://github.com/yangxin2/Trifunc/blob/master/%E7%95%8C%E9%9D%A2%E6%98%BE%E7%A4%BA%E8%AE%BE%E8%AE%A1.jpg)

## 2.整体框架

![image](https://github.com/yangxin2/Trifunc/blob/master/%E6%95%B4%E4%BD%93%E6%A1%86%E6%9E%B6.jpg)

## 3.数据流图：

![image](https://github.com/yangxin2/Trifunc/blob/master/%E6%95%B0%E6%8D%AE%E6%B5%81%E5%9B%BE.png)

# 详细设计：

## 1.界面显示部分

1）通过函数选择使用下拉选择框，选择计算sin、cos、arcsin、arctan；

2）输入框输入待计算信息；

3）输出框输出计算结果；

4）单位是结果，可以选择是弧度还是角度；

5）结果使用标签；

6）选择sin、cos时输入框后单位可以进行选择，输出框输出单位不可选；

7）选择arcsin、arctan时输入框后单位不可选择，输出框后单位可以选择；

8）输入框内可输入数字或算式，若输入内容超出定义域范围时计算按钮锁定，不可点击，即为输入错误。

## 2.功能部分

阶乘

幂函数

定义域收敛

绝对值

误差消除

## 3.功能函数

sin、cos、arcsin、arctan

角度转换弧度

弧度转换角度

