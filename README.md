# Photoacoustic Sensor Data Reconstruction

## Project Overview

This undergraduate research project investigates methods for reconstructing missing or inactive sensor data in photoacoustic imaging arrays.

The project uses Python to simulate sensor signals, model sensor failures, reconstruct missing measurements, and evaluate how sensor-data reconstruction affects the quality of Delay-and-Sum (DAS) images.

Two interpolation methods are investigated:

- Linear interpolation
- Cubic spline interpolation

Reconstruction quality is evaluated using Signal-to-Noise Ratio (SNR), Peak Signal-to-Noise Ratio (PSNR), and Structural Similarity Index Measure (SSIM).

## Project Objectives

1. Simulate synthetic photoacoustic sensor signals.
2. Implement a baseline 2D image reconstruction algorithm using Delay-and-Sum (DAS).
3. Simulate inactive sensors and different sensor-dropout patterns.
4. Reconstruct missing sensor signals using linear and cubic spline interpolation.
5. Compare reconstruction methods under different sensor-failure conditions.
6. Evaluate signal and image quality quantitatively.
7. Automate quality-metric calculations and visualize comparative results.
8. Organize reusable simulation and reconstruction functions into Python modules.

## Methods

### Signal Simulation

Synthetic Gaussian-shaped acoustic pulses are generated for a linear sensor array. Sensor positions, sampling times, source location, and the assumed speed of sound are used to model signal arrival times.

### Image Reconstruction

Delay-and-Sum (DAS) beamforming estimates image intensity by accumulating sensor-signal contributions at the predicted acoustic travel times.

### Missing Sensor Reconstruction

Inactive sensors are simulated using different dropout rates and failure patterns. Missing sensor signals are estimated using:

- Linear interpolation
- Cubic spline interpolation

### Quality Evaluation

The methods are evaluated using:

- **SNR:** Signal-to-Noise Ratio
- **PSNR:** Peak Signal-to-Noise Ratio
- **SSIM:** Structural Similarity Index Measure
- **MAE and RMSE:** Error measures used in selected signal and image comparisons

## Tools and Technologies

- Python
- NumPy
- SciPy
- Matplotlib
- scikit-image
- pandas
- Jupyter Notebook
- Git and GitHub
- Visual Studio Code

## Project Structure

```text
photoacoustic-sensor-reconstruction/
├── data/
├── notebooks/
│   ├── day03_04_numpy_basics.ipynb
│   ├── day24_das_implementation.ipynb
│   ├── day25_das_interpolation.ipynb
│   ├── day29_inactive_sensor_simulation.ipynb
│   ├── day30_linear_sensor_interpolation.ipynb
│   ├── day31_cubic_spline_interpolation.ipynb
│   ├── day39_das_linear_interpolation.ipynb
│   ├── day40_das_spline_interpolation.ipynb
│   ├── day50_automated_quality_evaluation.ipynb
│   ├── day51_results_visualization.ipynb
│   ├── day52_bar_chart_comparison.ipynb
│   └── day53_combined_quality_analysis.ipynb
├── outputs/
├── src/
│   ├── simulate.py
│   └── reconstruct.py
├── tests/
│   └── test_reconstruct.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Validation

The reusable DAS reconstruction function is implemented in `src/reconstruct.py`.

A basic validation test is available in `tests/test_reconstruct.py`. The test checks that:

- The reconstructed image has the expected dimensions.
- The image contains finite numerical values.
- The image has positive intensity.
- The maximum-intensity location matches the simulated source location in the current test configuration.

Current test configuration:

- Number of sensors: 32
- Number of time samples: 600
- Image grid: 100 × 100 pixels
- Simulated source location: (5 mm, 20 mm)

The test recovered the source location at (5.00 mm, 20.00 mm) for this configuration. This is a synthetic validation result, not a claim of equivalent accuracy on experimental data.

## Current Progress

The project has progressed through the simulation, DAS reconstruction, missing-sensor interpolation, quality evaluation, and result-visualization stages.

Completed work includes:

- NumPy fundamentals and signal visualization
- Synthetic sensor-array simulation
- Time-of-flight calculations
- DAS image reconstruction
- Inactive sensor simulation
- Linear and cubic spline interpolation
- SNR, PSNR, and SSIM evaluation
- Automated quality-metric analysis
- Quality-result visualizations
- Initial refactoring into reusable simulation and reconstruction modules
- A basic DAS validation test

## Limitations

The current implementation uses synthetic sensor signals and a simplified acoustic travel-time model. It is intended for studying reconstruction methods and their behavior under simulated sensor failures.

It is not yet a validated physical wave-propagation model and has not been established as a substitute for experimental photoacoustic data.

## Next Steps

- Continue modularizing the reconstruction workflow.
- Improve automated testing and reproducibility.
- Document the quality-metric results and their limitations.
- Refine the project instructions and prepare the repository for research presentation.

## Development Log

Daily experiments, implementation details, plots, and analysis are documented in the corresponding Jupyter notebooks in the `notebooks/` directory.
