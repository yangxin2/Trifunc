prePI = 3.1415926535897932		#提前设定一个π值,用于判断

def testFactorial(a):			#阶乘函数
    sum=1
    for i in range(1,a+1):
         sum*=i
    return sum


def testPower(x,t):			#幂函数
    m=1
    i=1
    while i<=t:
       m *= x
       i += 1
    return m


def inductionFormula(x):		#限制使定义域区间为-π到π，方便计算
    if x > prePI:
        while True:
            x -= (2 * prePI)
            if x <= prePI:
                y = x
                break
    elif x < (-1 * prePI):
        while True:
            x += (2 * prePI)
            if x >= (-1 * prePI):
                y = x
                break
    else: y = x
    return y


def testAbs(x):			#绝对值函数
    if x >= 0:
        x = x
    else:
        x = -x
    return x


def testRound(result):		#截尾函数，当结果应为+-0.5时，消除误差
    if(testAbs(result-0.5)<0.00000001):
        result = 0.5
    elif(testAbs(result+0.5)<0.00000001):
        result = -0.5
    elif (testAbs(result - 0) < 0.00000001):
        result = 0
    return result





# sin函数，使用泰勒展开公式计算

def testSin(x):       			#默认输入为弧度，角度弧度变化运用统一工具
    y =  inductionFormula(x)  		#诱导公式限制弧度制的输入为-π到π之间
    i=1                       		#泰勒展开式项数标识位
    f=1                      			#正负标识位
    result=0                     		#结果值
    num=0                    		#
    n=10                      		#泰勒展开式项数

    while True:
         g = 2*i-1            		#项数的值
         b = testFactorial(g)   		#阶乘结果
         t = testPower(y,g)     		#乘方结果
         result += t * f / b      		#单项结果累加
         i += 1
         num += 1
         f = -f               		#正负标识位
         if(num == n):
            break
    result = testRound(result)   		#自定义截尾函数，消除误差
    return result

#cos函数，由sin函数变换得出

def testCos(x):
    y = x + 0.5 * prePI          		#由变换公式实现sin函数与cos函数的转换
    return (testSin(y))



