def planet_orbit_eccentricity(
    eccentricity = 0.9,

):
    
    v = 0 
    d = 1
    from math import cos, sin

    r_storage = []

    while v < 361:
        r = (eccentricity * d) / (1 - eccentricity * cos(v))

        v += 1
        r_storage.append(r)
    
    print (min(r_storage) / max(r_storage))



planet_orbit_eccentricity(eccentricity = -1)