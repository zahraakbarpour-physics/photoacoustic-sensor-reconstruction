# Photoacoustic Sensor Data Reconstruction

## Project Overview

This undergraduate research project investigates methods for reconstructing missing or inactive sensor data in photoacoustic imaging arrays.

The project will simulate sensor data, introduce artificial sensor dropout, and reconstruct the missing signals using:

* Linear Interpolation
* Spline Interpolation

The effect of sensor-data reconstruction on photoacoustic image quality will be evaluated using:

* SNR
* PSNR
* SSIM

## Project Objectives

1. Simulate photoacoustic sensor data.
2. Implement a baseline image reconstruction algorithm using Delay-and-Sum (DAS).
3. Simulate defective or missing sensors.
4. Reconstruct missing sensor signals using interpolation methods.
5. Compare Linear and Spline Interpolation.
6. Evaluate the reconstructed images quantitatively.
7. Analyze the effect of different sensor dropout rates.

## Methods

The project will use Python-based numerical and scientific computing tools, including NumPy, SciPy, Matplotlib, and scikit-image.

Photoacoustic data will be simulated using an appropriate acoustic wave propagation simulation framework.

## Evaluation

The reconstruction methods will be evaluated using:

* Signal-to-Noise Ratio (SNR)
* Peak Signal-to-Noise Ratio (PSNR)
* Structural Similarity Index Measure (SSIM)

## Project Structure

```text
photoacoustic-sensor-reconstruction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│
├── notebooks/
│
├── README.md
│
└── .gitignore
```

## Status


- [x] Project initialization and Git workflow
- [x] NumPy fundamentals
- [x] Signal visualization and noise modeling
- [x] Missing sensor data and basic interpolation practice
- [x] Initial photoacoustic phantom and sensor-array simulation
- [x] Synthetic sensor signals and basic missing-signal reconstruction

**Current progress:** Days 1–20 of 60 (foundational simulation and signal reconstruction exercises).

**Next steps:** Implement a consistent 2D simulation, develop Delay-and-Sum (DAS) beamforming, and establish a baseline reconstruction before comparing interpolation methods.
## Development Log

### Day 2
- Practiced Git workflow.
- Learned how to stage, commit, and push changes.

- ## Days 3–4 — NumPy Fundamentals

### Goal
Learn the NumPy fundamentals required to work with sensor-array data and numerical matrices in the photoacoustic reconstruction project.

### What I Learned
- Created and manipulated NumPy arrays
- Worked with multidimensional arrays and understood `shape` and `ndim`
- Practiced array indexing and slicing
- Selected individual sensors and time samples from a sensor matrix
- Learned how `axis=0` and `axis=1` affect array operations
- Applied statistical operations:
  - `mean`
  - `min`
  - `max`
  - `std`
  - `sum`
- Used `argmax` to identify the sensor with the highest mean value
- Worked with simulated sensor data represented as a `128 × 2000` matrix

### Project Connection
The simulated sensor matrix represents:

- **128 sensors**
- **2000 time samples per sensor**

This structure will later be used to simulate missing sensor data, apply interpolation methods, and reconstruct the photoacoustic image.

### Practice Notebook
All exercises and experiments from these two days were documented separately in:

`notebooks/day03_04_numpy_basics.ipynb`

### Status
- [x] NumPy basics
- [x] Array indexing and slicing
- [x] Axis operations
- [x] Statistical operations
- [x] Sensor-matrix practice
- [x] NumPy fundamentals completed

## Day 5 — Signal Visualization and Noise Modeling

**Objective:** Develop fundamental signal visualization techniques and simulate measurement noise using Python.

### Work Completed

* Generated a synthetic sinusoidal signal using NumPy.
* Visualized signals using Matplotlib, including appropriate titles, axis labels, legends, and grid lines.
* Simulated measurement noise using a random noise model.
* Compared the original signal with its noisy counterpart to understand the effects of noise on signal quality.
* Saved the generated plots for documentation and future analysis.

### Key Concepts

* Numerical signal generation with NumPy
* Signal visualization using Matplotlib
* Random noise modeling
* Comparison of ideal and noisy measurements
* Exporting figures for reproducible scientific documentation

### Project Relevance

This work establishes the foundation for analyzing sensor measurements under realistic conditions. Understanding the effects of noise is essential for evaluating reconstruction methods and assessing the quality of recovered photoacoustic sensor data.

**Tools:** Python, NumPy, Matplotlib

---

## Day 6 — Missing Sensor Data and Linear Interpolation

**Objective:** Investigate missing sensor measurements and implement linear interpolation as an initial data reconstruction technique.

### Work Completed

* Represented sensor measurements as numerical arrays and visualized them as a matrix.
* Simulated missing measurements by introducing `NaN` values into the dataset.
* Identified missing entries using NumPy's missing-value detection capabilities.
* Implemented linear interpolation using `scipy.interpolate.interp1d`.
* Reconstructed a missing signal value from neighboring valid measurements.
* Visualized the sensor matrix, missing-data pattern, and reconstructed signal.
* Saved the resulting figures and documented the implementation in a Jupyter notebook.

### Key Concepts

* Missing-data representation and detection
* Sensor measurement matrices
* Linear interpolation
* Signal reconstruction from valid samples
* Scientific visualization and numerical analysis

### Project Relevance

Missing or inactive sensors can produce incomplete measurements in photoacoustic imaging systems. Linear interpolation provides a simple baseline for estimating missing values from available data. This baseline will support future comparisons with more advanced reconstruction methods, including cubic interpolation.
---

## Days 9–12 — Photoacoustic Phantom and Sensor Array

### Objective
Build a simple photoacoustic phantom and explore the geometry of an acoustic sensor array.

### Work Completed
- Created a simple 2D phantom representing relative optical absorption.
- Calculated an initial pressure distribution using a simplified model.
- Generated a circular array of 16 sensors.
- Calculated source-to-sensor distances.
- Estimated acoustic time-of-flight (ToF) values using an assumed speed of sound.
- Investigated how source position affects sensor arrival times.

### Key Concepts
- Photoacoustic phantom modeling
- Sensor-array geometry
- Euclidean distance
- Acoustic time-of-flight
- Speed of sound and arrival-time estimation

**Tools:** Python, NumPy, Matplotlib

## Days 13–16 — Synthetic Signals and Missing Sensor Data

### Objective
Generate simple synthetic sensor signals and investigate the effect of missing sensors.

### Work Completed
- Generated Gaussian-shaped synthetic acoustic pulses.
- Visualized signals from multiple sensors.
- Simulated a missing sensor by replacing its signal with `NaN` values.
- Estimated a missing signal using neighboring sensor measurements.

### Key Concepts
- Synthetic signal generation
- Time-domain signal visualization
- Missing sensor simulation
- Basic signal interpolation

**Tools:** Python, NumPy, Matplotlib

## Days 17–20 — Reconstruction Error and Method Comparison

### Objective
Evaluate simple missing-signal reconstruction methods and compare their performance.

### Work Completed
- Calculated mean squared error (MSE) and root mean squared error (RMSE).
- Compared original and reconstructed synthetic signals.
- Improved the initial reconstruction by estimating the missing sensor's arrival time.
- Compared neighboring-signal averaging with arrival-time-based Gaussian pulse reconstruction.
- Saved figures illustrating the signals, missing data, reconstruction results, and errors.

### Key Concepts
- Reconstruction error metrics
- MSE and RMSE
- Signal comparison
- Arrival-time estimation
- Limitations of simplified synthetic models

### Important Limitation
These exercises use simplified synthetic signals and do not yet represent a complete physical acoustic wave-propagation model or a full 2D image reconstruction pipeline.

### Next Steps
- Develop a consistent 2D acoustic simulation.
- Implement Delay-and-Sum (DAS) beamforming.
- Reconstruct a baseline image using complete sensor data.
- Introduce sensor dropout and compare interpolation methods.

**Tools:** Python, NumPy, Matplotlib


**Tools:** Python, NumPy, SciPy, Matplotlib, Jupyter Notebook

