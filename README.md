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
