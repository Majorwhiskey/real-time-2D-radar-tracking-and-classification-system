import numpy as np

class ParticleFilter2D:
    def __init__(self, num_particles=1000, bounds=[0, 100]):
        self.N = num_particles
        self.bounds = bounds
        self.particles = np.random.uniform(bounds[0], bounds[1], size=(self.N, 2))
        self.weights = np.ones(self.N) / self.N

    def predict(self, motion_std=1.0):
        noise = np.random.randn(self.N, 2) * motion_std
        self.particles += noise
        self.particles = np.clip(self.particles, self.bounds[0], self.bounds[1])

    def update(self, measurement, measurement_std=5.0):
        dists = np.linalg.norm(self.particles - measurement, axis=1)
        self.weights = np.exp(-0.5 * (dists / measurement_std) ** 2)
        self.weights += 1e-300
        self.weights /= np.sum(self.weights)

    def resample(self):
        indices = np.random.choice(self.N, self.N, p=self.weights)
        self.particles = self.particles[indices]
        self.weights.fill(1.0 / self.N)

    def estimate(self):
        return np.average(self.particles, axis=0, weights=self.weights)
