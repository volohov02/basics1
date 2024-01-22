def calc():
    k_1 = 339.31
    k_2 = 265.21
    x_2 = 0.08
    E_2 = 2.13
    W = 12.42
    m = 0.87
    v = 6.79
    answer = k_2*x_2**2*(k_1+k_2)/(k_1*v**2)
    return answer