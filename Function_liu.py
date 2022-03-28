

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


#参数定义
myPI = 3.1415926535897932



def absxxxx(x):
    if x >= 0 :
        return x
    else:
        return -x

def invert_angle_to_rad(angles):
    angle = angles * myPI / 180
    return angle





