import numpy as np
import matplotlib.pyplot as plt

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def plot_3d_path(gt_path, est_path, title="3D Tracking"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(*gt_path.T, 'g--', label='Ground Truth')
    ax.plot(*est_path.T, 'r-', label='Estimated Path')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()
