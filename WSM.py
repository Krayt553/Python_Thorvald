import numpy as np

def nulte_led(A, Z):
    masseP = 1.007825 * Z * 931.49         #MeV

    masseN = 1.008665 * (A - Z) * 931.49    #MeV

    return(masseP + masseN)

def første_led(A):
    a1 = 15.75              #Mev

    return(-(a1 * A))

def andet_led(A):
    a2 = 17.8               #MeV

    return(a2 * A ** (2/3))

def tredje_led(A, Z):
    a3 = 0.711              #MeV
    tæller = Z ** 2
    nævner = A ** (1/3)


    return(a3 * (tæller/nævner))

def fjerde_led(A, Z):
    a4 = 23.7               #MeV
    tæller = (A / 2 - Z) **2

    return(a4 * (tæller / A))

def fermi_led(A, Z):
    fermiLed = 11.18 / (A ** (-3/4))        #MeV

    if (A % 2) != 0:
        return(0)
    else:
        if (Z % 2) != 0:
            return(+fermiLed)
        if (Z % 2) == 0:
            return(-fermiLed)

def M(A, Z):
    return(nulte_led(A, Z) + første_led(A) + andet_led(A) + tredje_led(A, Z) + fjerde_led(A, Z) + fermi_led(A, Z))

def massedefekt(A, Z):
    masse = M(A, Z) / A

    masseNukleon = 1.008665 * 931.44 - masse

    return(masseNukleon)

print(f"{massedefekt(190, 76)} MeV")


for i in range(50):
    A = 140 + i * 2
    Z = 57 + i
    
    print(f"{A},{Z} :  {massedefekt(A,Z)} MeV")
