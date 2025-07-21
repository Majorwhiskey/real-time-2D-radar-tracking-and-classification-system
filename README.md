# Real-Time Radar Target Tracking and Classification

This project implements a simulated real-time 2D radar tracking and classification system using:

- Kalman Filter for tracking
- Particle Filter for nonlinear tracking
- SVM for motion classification (fast vs slow)
- Real-time visualization using matplotlib animation

## Files
- `kalman_tracker.py`: Kalman filter implementation
- `particle_tracker.py`: Particle filter implementation
- `simulate_targets.py`: Target motion simulation
- `classify_targets.py`: SVM training and testing
- `utils.py`: Shared functions for motion and plotting
- `visualization.py`: Live radar visualization

## Getting Started
```bash
pip install -r requirements.txt
python visualization.py
