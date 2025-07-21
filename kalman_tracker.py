import numpy as np

class KalmanTracker3D:
    def __init__(self, dt=1.0, process_noise=1.0, measurement_noise=10.0):
        self.dt = dt
        self.A = np.eye(6)
        self.A[:3, 3:] = np.eye(3) * dt
        self.H = np.eye(3, 6)
        self.Q = np.eye(6) * process_noise
        self.R = np.eye(3) * measurement_noise
        self.P = np.eye(6) * 500.0
        self.x = np.zeros((6, 1))  # [x, y, z, vx, vy, vz]

    def predict(self):
        self.x = self.A @ self.x
        self.P = self.A @ self.P @ self.A.T + self.Q
        return self.x[:3].flatten()

    def update(self, z):
        z = np.reshape(z, (3, 1))
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x += K @ y
        self.P = (np.eye(6) - K @ self.H) @ self.P
        return self.x[:3].flatten()
