import numpy as np

def nulte_led(A, Z):
    masseP = 1.007825 * Z * 931.49         #MeV

    masseN = 1.008665 * (A - Z) * 931.49    #MeV

    return(masseP + masseN)

def volumen_led(A):
    a1 = 15.75              #Mev

    return(a1 * A)

def overflade_led(A):
    a2 = 17.8               #MeV

    return(a2 * (A ** (2/3)))

def coulomb_led(A, Z):
    a3 = 0.711              #MeV
    tæller = Z * (Z - 1)
    nævner = A ** (1/3)


    return(a3 * (tæller/nævner))

def assymetri_led(A, Z):
    a4 = 23.7               #MeV
    tæller = (A - 2*Z) **2

    return(a4 * (tæller / A))

def fermi_led(A, Z):
    fermiLed = 34 / (A ** (3/4))        #MeV

    if (A % 2) != 0:
        return(0)
    else:
        if (Z % 2) != 0:
            return(+fermiLed)
        if (Z % 2) == 0:
            return(-fermiLed)

def M(A, Z):
    bindingsEnergien = volumen_led(A) - overflade_led(A) - coulomb_led(A, Z) - assymetri_led(A, Z) + fermi_led(A, Z)
    MeVtoJoules = bindingsEnergien * 1.6E-13
    
    return(MeVtoJoules)

def massedefekt(A, Z):
    bindingsenergi = M(A, Z) / ((3.00E+8) ** 2)
    atomUnitToMeV = bindingsenergi * 6.02E+26

    masseDefekt = (atomUnitToMeV / A) * 931.5

    return(masseDefekt)

print(f"{massedefekt(116, 57)} MeV")

