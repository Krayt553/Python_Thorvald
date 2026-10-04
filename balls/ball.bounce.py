def simulate_ball_drop(
    initial_height=10.0,
    gravity=9.81,
    restitution=0.75,
    #bolden er en tennisbold
):
    """Simulate a ball dropping from an initial height under gravity."""
    time_step = 0.05
    height = float(initial_height)
    velocity = 0.0
    time = 0.0

    """store variables in lists"""
    height_storage = []
    velocity_storage = []
    time_storage = []
    
    while time < 100: 
        velocity += gravity * time_step
        height -= velocity * time_step
        time += time_step

        height_storage.append(height)
        velocity_storage.append(velocity)
        time_storage.append(time)

        if height <= 0:
            height = 0
            velocity = -velocity * restitution

    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    fig, ax = plt.subplots()
    ball, = ax.plot([], [], 'ro')

    def update(frame):
        ball.set_data([0], [height_storage[frame]])
        return ball,

    ani = FuncAnimation(fig, update, frames=len(height_storage), interval=10)
    
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, initial_height)

    plt.show()

if __name__ == "__main__":
    simulate_ball_drop(initial_height=1.5, gravity=9.81, restitution=0.75)
