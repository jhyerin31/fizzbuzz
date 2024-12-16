from math import sqrt

def fibo(num):
    """
    fibonacci sequence를 구하는 함수 입니다.
    """
    #if num <2 :
        #return num
    #else:
        #return fibo(num-1) + fibo(num-2)

    phi = (1 + sqrt(5)) / 2
    phi2 = (1 - sqrt(5)) / 2
    return round(pow(phi,num) - pow(phi2,num) / sqrt(5))
print(fibo(5))
