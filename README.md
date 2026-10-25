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

### Days 1–2 — Project Setup and Git Workflow
- Initialized the project and established a Git/GitHub workflow.
- Practiced staging, committing, and pushing changes.

### Days 3–4 — NumPy Fundamentals
- Practiced array creation, indexing, slicing, multidimensional arrays, and axis operations.
- Applied statistical functions to simulated sensor matrices.
- Documented exercises in `day03_04_numpy_basics.ipynb`.

### Day 5 — Signal Visualization
- Generated and visualized synthetic signals using NumPy and Matplotlib.
- Explored random noise and saved figures.

### Day 6 — Missing Data and Linear Interpolation
- Represented missing measurements using `NaN`.
- Practiced missing-value detection and linear interpolation.

### Days 7–8
- No separate notebook is currently listed for these days.

### Days 9–12 — Photoacoustic Phantom and Sensor Array
- Built a simplified 2D phantom.
- Explored sensor-array geometry, source-to-sensor distances, and acoustic time of flight.

### Days 13–16 — Synthetic Signals
- Generated synthetic Gaussian-shaped acoustic pulses.
- Explored sensor signals and simulated missing measurements.

### Days 17–20 — Initial Reconstruction Exercises
- Compared simplified signal-reconstruction approaches.
- Calculated MSE and RMSE and examined arrival-time-based signal estimates.

### Day 21
- Continued the transition from foundational exercises to the photoacoustic reconstruction workflow.
- See the corresponding project notebook and subsequent implementation notebooks for details.

### Day 22 — Time-of-Flight Calculation
- Calculated acoustic travel times for sensor measurements.
- Documented the work in `day22_tof_calculation.ipynb`.

### Day 23 — Delay-and-Sum Fundamentals
- Developed the initial Delay-and-Sum reconstruction workflow.
- Documented the work in `day23_delay_and_sum.ipynb`.

### Day 24 — DAS Implementation
- Implemented a 2D Delay-and-Sum reconstruction function.
- Documented the implementation in `day24_das_implementation.ipynb`.

### Day 25 — DAS with Interpolation
- Combined DAS reconstruction with interpolated sensor signals.
- Saved reconstruction results in the project workflow.

### Day 26 — DAS Comparison
- Compared DAS reconstruction approaches and documented the results.

### Day 27 — Ground-Truth Reference
- Established a reference image/source configuration for subsequent comparisons.

### Day 28 — Image Quality Metrics
- Introduced image-quality evaluation for reconstruction experiments.

### Day 29 — Inactive Sensor Simulation
- Simulated inactive sensors in the array.
- Investigated the impact of missing sensor measurements.

### Day 30 — Linear Sensor Interpolation
- Implemented linear interpolation for missing sensor signals.
- Compared reconstructed signals with reference measurements.

### Day 31 — Cubic Spline Interpolation
- Applied cubic spline interpolation to missing sensor data.

### Day 32 — Missing Sensor Ratio Analysis
- Investigated how the proportion of missing sensors affects reconstruction.

### Day 33 — Sensor Failure Patterns
- Compared different patterns of inactive sensors.

### Day 34 — Linear `interp1d`
- Explored linear interpolation using SciPy's `interp1d`.

### Day 35 — Linear Interpolation Failure Patterns
- Compared linear interpolation performance under different sensor-failure patterns.

### Day 36 — Cubic Spline Interpolation
- Continued implementing and evaluating cubic spline reconstruction.

### Day 37 — Spline Missing-Ratio Analysis
- Evaluated spline interpolation at different missing-sensor ratios.

### Day 38 — Spline Failure-Pattern Comparison
- Investigated spline interpolation performance under different failure patterns.

### Day 39 — DAS with Linear Interpolation
- Integrated linear interpolation into the DAS reconstruction workflow.

### Day 40 — DAS with Spline Interpolation
- Integrated cubic spline interpolation into DAS reconstruction.
- Compared reconstruction errors between interpolation approaches.

### Day 41 — SNR Evaluation
- Introduced Signal-to-Noise Ratio evaluation for reconstructed data.

### Day 42 — SNR Robustness Analysis
- Compared SNR under different missing-sensor conditions.
- Recorded an SNR value of approximately 28.75 dB in the relevant experiment.

### Day 43 — SNR Validation
- Continued validating the SNR evaluation workflow.

### Day 44 — PSNR Evaluation
- Evaluated Peak Signal-to-Noise Ratio for reconstructed images.
- In one 25% random-dropout experiment, recorded PSNR values of 23.38 dB for incomplete data, 59.03 dB for linear interpolation, and 75.21 dB for spline interpolation.

### Day 45 — PSNR Robustness Analysis
- Investigated PSNR performance under different missing-sensor conditions.

### Day 46 — PSNR Failure Patterns
- Compared PSNR results across sensor-failure patterns.

### Day 47 — SSIM Evaluation
- Introduced Structural Similarity Index Measure evaluation.

### Day 48 — SSIM Robustness Analysis
- Investigated SSIM performance under different missing-sensor conditions.

### Day 49 — Quality Metrics Comparison
- Brought multiple image-quality metrics together for comparative analysis.

### Day 50 — Automated Quality Evaluation
- Automated quality-metric calculations.
- Organized results for different dropout levels and reconstruction methods.

### Day 51 — Results Visualization
- Visualized quality metrics from the automated evaluation results.

### Day 52 — Bar Chart Comparison
- Created comparative bar charts for the reconstruction methods and quality metrics.

### Day 53 — Combined Quality Analysis
- Combined quality-metric visualizations to support a broader comparison of reconstruction methods.

### Day 54 — Simulation Module
- Refactored synthetic sensor-signal generation into `src/simulate.py`.
- Verified that the module runs and generates a signal matrix with 32 sensors and 600 time samples.

### Day 55 — DAS Reconstruction Module and Test
- Refactored the `delay_and_sum` function into `src/reconstruct.py`.
- Created `tests/test_reconstruct.py` to validate the reconstructed image.
- Verified the expected image dimensions and finite intensity values.
- Confirmed that the estimated source location matched (5 mm, 20 mm) in the synthetic test configuration.
- In the current synthetic test, the estimated source location matched the configured location of (5 mm, 20 mm).
- Committed and pushed the changes to GitHub.

### Day 56 — Documentation
- Updated the README to reflect the current project structure, methods, validation, and development history.

### Day 57 — Automated Reconstruction Pipeline
- Created `src/run_pipeline.py` to connect signal simulation and DAS image reconstruction.
- Executed the pipeline successfully.
- Verified the reconstructed image dimensions and estimated source location.

### Day 58 — Saving Reconstruction Results
- Updated the pipeline to save the DAS reconstruction image and numerical results.
- Saved `day58_das_reconstruction.png` and `day58_das_results.json` in the `outputs/` directory.
- Verified that the changes were committed and pushed to GitHub.

### Day 59 — Testing and Validation
- Installed `pytest` for automated testing.
- Ran `python -m pytest -v`.
- Passed the DAS reconstruction test.
- Executed the reconstruction pipeline successfully.
- Confirmed that the local Git working tree was clean and synchronized with `origin/main`.