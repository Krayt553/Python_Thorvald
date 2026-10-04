def planet_orbit(
    r_perihelion = 1,
    r_aphelion = 10,
    mass = 1,
):
    
    import math

    r_perihelion = r_perihelion * 1.495979e+11
    r_aphelion = r_aphelion * 1.495979e+11
    mass = mass * 1.989 * 10**30
    r = r_perihelion
    semi_major = (r_perihelion + r_aphelion) / 2

    r = r_perihelion
    Grav_konstant = 6.67430e-11
    T = math.sqrt((4 * 3.14159**2 * semi_major**3) / (Grav_konstant * mass))
    velocity = math.sqrt(Grav_konstant * mass * (2/r - 1/semi_major))
    dt = T / 3600
    time = 0

    x = r_perihelion 
    y = 0
    vy = velocity 
    vx = 0

    x_storage = []
    y_storage = []
    r_storage = []

    while time < T*5: 
        ax = -Grav_konstant * mass * x / (r**3)
        ay = -Grav_konstant * mass * y / (r**3)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        
        time += dt
        r = math.sqrt(x**2 + y**2)

        x_storage.append(x)
        y_storage.append(y)
        r_storage.append(r)

    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    planet, = ax.plot([], [], 'ro')
    sun, = ax.plot([], [], 'yo')
    path, = ax.plot([], [], 'b-', linewidth=1)

    def update(frame):
        planet.set_data([x_storage[frame]], [y_storage[frame]])
        sun.set_data([0], [0])
        path.set_data(x_storage[:frame + 1], y_storage[:frame + 1])
        return planet, sun, path

    frame_step = 15
    ani = FuncAnimation(fig, update, frames=range(0, len(x_storage), frame_step), interval=0.05)
    
    ax.set_xlim(-1.5*r_aphelion, 1.5*r_aphelion)
    ax.set_ylim(-1.5*r_aphelion, 1.5*r_aphelion)

    plt.show()

planet_orbit(r_perihelion = 0.3075, r_aphelion = 0.4667, mass = 1)