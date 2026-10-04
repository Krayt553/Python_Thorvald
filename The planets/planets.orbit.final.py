def max_timestep(planets_params, mass, Grav_konstant): 
    import math

    max_aphelion = max(p["r_aphelion"] for p in planets_params.values())
    max_perihelion = max(p["r_perihelion"] for p in planets_params.values())
    max_semimajor = 1.495979e+11 * (max_aphelion + max_perihelion) / 2 
    
    numerator = 4 * pi **2 * max_semimajor **3
    denominator = Grav_konstant * mass
    T = math.sqrt(numerator / denominator)

    return(T)

def planet_orbit(r_perihelion, r_aphelion, mass,):
    
    import math
    from math import pi

    r_perihelion = r_perihelion * 1.495979e+11
    r_aphelion = r_aphelion * 1.495979e+11
    mass = mass * 1.989 * 10**30
    r = r_perihelion

    Grav_konstant = 6.67430e-11
    vis_viva = (2 / r - 1 / ((r_perihelion + r_aphelion) / 2))
    velocity = math.sqrt(Grav_konstant * mass * vis_viva)
    
    max_aphelion = max(p["r_aphelion"] for p in planets_params.values())
    max_perihelion = max(p["r_perihelion"] for p in planets_params.values())
    max_semimajor = 1.495979e+11 * (max_aphelion + max_perihelion) / 2 

    numerator = 4 * pi **2 * max_semimajor **3
    denominator = Grav_konstant * mass
    T = math.sqrt(numerator / denominator)

    dt = T / 36000
    time = 0

    x = r_perihelion 
    y = 0
    vy = velocity 
    vx = 0

    x_storage = []
    y_storage = []

    
    while time < T * 3: 
        ax = -Grav_konstant * mass * x / (r **3)
        ay = -Grav_konstant * mass * y / (r **3)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        
        time += dt
        r = math.hypot(x, y)

        x_storage.append(x)
        y_storage.append(y)

    return x_storage, y_storage

planets_params = {
    #"mercury": {"r_perihelion": 0.3075, "r_aphelion": 0.4667, "mass": 1},
    #"earth": {"r_perihelion": 1.0, "r_aphelion": 1.0, "mass": 1},
    #"venus": {"r_perihelion": 0.7184, "r_aphelion": 0.7282, "mass": 1},
    #"mars" : {"r_perihelion": 1.381, "r_aphelion": 1.666, "mass": 1},
    "Halley's Comet" : {"r_perihelion": 0.59, "r_aphelion": 35.25, "mass": 1},
    "Neptune" : {"r_perihelion": 29.77, "r_aphelion": 30.44, "mass": 1},
    #"Saturn" : {"r_perihelion": 9, "r_aphelion": 10.1, "mass": 1},
    #"Jupiter" : {"r_perihelion": 4.95, "r_aphelion": 5.46, "mass": 1},
    }

planets_trajectories = {
    
}

for p in planets_params:
    x_storage, y_storage = planet_orbit(**planets_params[p])
    planets_trajectories[p] = (x_storage, y_storage)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_aspect('equal')

sun, = ax.plot([], [], 'yo')
planet_lines = {name: ax.plot([], [], 'o')[0] for name in planets_trajectories}
path_lines = {name: ax.plot([], [], '-', linewidth=1)[0] for name in planets_trajectories}

def init():
    sun.set_data([], [])
    for name, (x_storage, y_storage) in planets_trajectories.items():
        planet_lines[name].set_data([],[])
        path_lines[name].set_data([],[])

    return sun, *planet_lines.values(), *path_lines.values()

def update(frame):
    sun.set_data([0], [0])
    
    for name, (x_storage, y_storage) in planets_trajectories.items():
        planet_lines[name].set_data([x_storage[frame]], [y_storage[frame]])
        path_lines[name].set_data(x_storage, y_storage)

    return sun, *planet_lines.values(), *path_lines.values()

frame_step = 20
ani = FuncAnimation(
    fig, update, 
    frames = range(0, min(len(traj[0]) for traj in planets_trajectories.values()), frame_step), 
    init_func = init,
    interval = 20,
    blit = True,
    )

max_aphelion = 1.495979e+11 * max(p["r_aphelion"] for p in planets_params.values())

ax.set_xlim(-1.1 * max_aphelion, 1.1 * max_aphelion)
ax.set_ylim(-1.1 * max_aphelion, 1.1 * max_aphelion)

plt.show()

