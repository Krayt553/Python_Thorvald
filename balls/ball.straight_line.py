def simulate_straight_line(
    a = 2,    
    b = 2
):
    x = 0  
    y = 0 + b

    x_storage = []
    y_storage = []

    while x < 100:
        x += 1
        y = a * x + b
        
        x_storage.append(x)
        y_storage.append(y)
    
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    fig, ax = plt.subplots()
    ball, = ax.plot([], [], 'ro')

    def update(frame):
        ball.set_data([x_storage[frame]], [y_storage[frame]])
        return ball,

    ani = FuncAnimation(fig, update, frames=len(x_storage), interval=10)
    
    ax.set_xlim(-1, 100)
    ax.set_ylim(-1, 100*a)

    plt.show()

simulate_straight_line(a = 3, b = 20)
