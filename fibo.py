from math import sqrt
def fibo(num):
    phi = (1 + sqrt(5)) / 2
    phi2 = (1 - sqrt(5)) / 2
    return round(pow(phi,num) - pow(phi2,num) / sqrt(5))
print(fibo(5))
