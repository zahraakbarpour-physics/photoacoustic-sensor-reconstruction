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

Project initialization — Day 1 of 60.
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
