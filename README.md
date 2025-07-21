# Real-time 3D Radar Tracking and Classification System 📡

## Overview

This project implements a **real-time 2D radar target tracking and classification system** using advanced filtering and machine learning techniques. It's designed to simulate noisy radar measurements, apply state estimation using **Kalman Filters** and **Particle Filters**, and classify target motion using **Support Vector Machines (SVMs)**. This system is perfect for those new to radar tracking, state estimation, and real-time data visualization in Python.

## ✨ Key Features

  * **3D Kalman Filter Tracking**: Accurately estimates the position and velocity of moving objects in a 3D space, even with noisy measurements.
  * **2D Particle Filter**: Addresses nonlinear motion tracking challenges, providing robust state estimation for complex trajectories.
  * **SVM-based Motion Classification**: Classifies different types of target motion based on their characteristics.
  * **Real-time 3D Plotting**: Visualizes true, noisy, and estimated trajectories simultaneously, offering insightful real-time feedback.
  * **Synthetic Target Simulation**: Generates realistic synthetic target data for comprehensive testing and development.

## ⚙️ Technologies Used

The project is primarily developed in **Python** and leverages the following core components:

  * `kalman_tracker.py`: Implements the core Kalman Filter logic for state estimation.
  * `particle_tracker.py`: Contains the Particle Filter implementation for handling non-linear dynamics.
  * `simulate_targets.py`: Manages the generation and simulation of various target motions.
  * `classify_targets.py`: Handles the training and inference of SVM models for target classification.
  * `utils.py`: Provides essential utility functions, including distance calculations and plotting tools.

## 🚀 Installation

To get started with the project, you'll need to install the required Python packages.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Majorwhiskey/Real-time-2D-radar-tracking-and-classification-system.git
    cd Real-time-2D-radar-tracking-and-classification-system
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## 🏃 How to Run

After installation, you can run the different components of the system. You'll likely want to run the simulation, tracking, and classification scripts to see the system in action.

While specific execution instructions are not detailed in the repository, you can typically run the main components as follows:

  * To simulate targets (and potentially visualize them):
    ```bash
    python simulate_targets.py
    ```
  * To run the Kalman Filter tracker:
    ```bash
    python kalman_tracker.py
    ```
  * To run the Particle Filter tracker:
    ```bash
    python particle_tracker.py
    ```
  * To classify targets using SVM:
    ```bash
    python classify_targets.py
    ```

You might need to open and inspect each Python file to understand specific command-line arguments or configurations.

-----
