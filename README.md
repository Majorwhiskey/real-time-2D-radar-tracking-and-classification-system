# Real-Time Radar Target Tracking and Classification

This project simulates radar target tracking using Kalman and Particle Filters, and classifies targets based on motion features using SVM.

## Features
- 3D Kalman Filter tracking
- 2D Particle Filter for nonlinear motion
- SVM-based motion classification
- Real-time 3D plotting
- Synthetic target simulation

## Files
- `kalman_tracker.py`: Kalman Filter logic
- `particle_tracker.py`: Particle Filter logic
- `simulate_targets.py`: Target motion simulator
- `classify_targets.py`: SVM training and inference
- `utils.py`: Distance and plotting tools

## Install
```bash
pip install -r requirements.txt
