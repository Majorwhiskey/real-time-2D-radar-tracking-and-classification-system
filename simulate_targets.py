import numpy as np

def simulate_linear_motion(timesteps, velocity=(1, 1, 1), start=(0, 0, 0)):
    positions = []
    pos = np.array(start, dtype=float)
    vel = np.array(velocity, dtype=float)
    for _ in range(timesteps):
        pos += vel
        positions.append(pos + np.random.randn(3))  # add noise
    return np.array(positions)
