def calc():
    k_1 = 250.29
    k_2 = 386.2
    x_2 = 0.03
    E_2 = 3.14
    W = 17.89
    m = 1.64
    v = 3.69
    answer = -k_2**2*x_2**2/(k_2*x_2**2-m*v**2)
    return answer