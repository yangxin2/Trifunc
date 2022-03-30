
myPI = 3.1415926535897932
##############-sin函数-##################
def mySin(x):       #inputFlag为1，角度，inputFlag为2，弧度

    y =  inductionFormula(x)  #诱导公式限制弧度制的输入为-π到π之间
    i=1                       #泰勒展开式项数标识位
    f=1                       #正负标识位
    result=0                      #结果值
    num=0
    n=10                      #泰勒展开式项数

    while True:
         g = 2*i-1            #项数的值
         b = myFactorial(g)   #阶乘结果
         t = myPower(y,g)     #乘方结果
         result += t * f / b      #单项结果累加
         i += 1
         num += 1
         f = -f               #正负标识位
         if(num == n):
            break
    result = myRound(result)   #自定义截尾函数，消除误差
    return result
#####################-cos函数-########################
def myCos(x):       #inputFlag为1，角度，inputFlag为2，弧度
    y = x + 0.5 * myPI          #cos转换为sin
    return (mySin(y))

################-arcsin函数-######################
def asin(x):
    result = x
    result_a = 1.0
    result_b = 1.0
    result_c = 1.0
    ii = 0
    if (x == 1 ):
        result = 90
    elif (x == -1):
        result = -90
    elif ((x < 1) and (x > -1)):
        for i in range(0, 15, 1):
            for ii in range(0,2*i+1, 1 ):
                result_a *= (2 * ii + 1) / (2 * ii +2)
                result_b *= x * x
            result_b *= x
            result_c = result_a / (ii + 2)
            result += result_c * result_b
            result_a = 1.0; result_b = 1.0
    return result
####################-arctan函数-##########################
def atan(x):
    mult = 0
    sum = 0
    xx = 0
    sign = 1
    if (x == 1):
        sum = myPI / 4
    elif (x == -1):
        sum = -myPI / 4
    elif ((x > 1) or (x < -1)):
        mult = 1 / x
        sign = -sign
        xx = mult * mult
        for i in range(1, 300, 2):
            sum += mult * sign / i
            mult *= xx
        if (x > 1):
            sum = sum + myPI / 2
        elif (x < -1):
            sum = -(myPI / 2 - sum)
        else:
            sum = sum
    elif ((x > -1) or (x < 1)):
        sum = x
        x_pow = x
        item = 1
        # 定义正负与阶数
        n = 1
        fact = 1
        sign = 1
        while ((absxxxx(item) > 0.000001) or (item == 0.00)):
            fact = fact * (n + 1) * (n + 2)
            x_pow *= x * x
            sign = -sign
            item = x_pow / (n + 2) * sign
            sum += item
            n += 2
    return sum



######################-阶乘函数-###################
def myFactorial(a):
    sum=1
    for i in range(1,a+1):
         sum*=i
    return sum

#####################-幂函数-####################

def myPower(x,t):
    m=1
    i=1
    while i<=t:
       m *= x
       i += 1
    return m

#######################-诱导公式使定义域收敛-###################
def inductionFormula(x):
    if x > myPI:
        while True:
            x -= (2 * myPI)
            if x <= myPI:
                y = x
                break
    elif x < (-1 * myPI):
        while True:
            x += (2 * myPI)
            if x >= (-1 * myPI):
                y = x
                break
    else: y = x
    return y

####################-绝对值函数-###########################

def myAbs(x):
    if x >= 0:
        x = x
    else:
        x = -x
    return x

#############-截尾函数，当结果应为+-0.5时，消除误差-###########

def myRound(result):
    if(myAbs(result-0.5)<0.00000001):
        result = 0.5
    elif(myAbs(result+0.5)<0.00000001):
        result = -0.5
    elif (myAbs(result - 0) < 0.00000001):
        result = 0
    return result

###################-绝对值-######################
def absxxxx(x):
    if x >= 0 :
        return x
    else:
        return -x
#############-弧度转化为角度-###################
def invert_angle_to_rad(angles):
    angle = angles * myPI / 180
    return angle
