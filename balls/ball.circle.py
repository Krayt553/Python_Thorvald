def simulate_circle(
    radius = 5, 
    k = 0,
    h = 0
):
    x = 0  
    y = 0 
    v = 0

    x_storage = []
    y_storage = []

    from math import sin, cos
    import math

    while v < 361:
        y = radius * sin(math.radians(v)) + h
        x = radius * cos(math.radians(v)) + k
        v += 2

        x_storage.append(x)
        y_storage.append(y)
    
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    fig, ax = plt.subplots()
    ax.grid = True
    ax.set_aspect('equal')
    ball, = ax.plot([], [], 'ro')

    def update(frame):
        ball.set_data([x_storage[frame]], [y_storage[frame]])
        return ball,

    ani = FuncAnimation(fig, update, frames=len(x_storage), interval=0.05)
    
    ax.set_xlim(-2*radius, 2*radius)
    ax.set_ylim(-2*radius, 2*radius)

    plt.show()

simulate_circle(radius = 20, k = 0, h = 0)
