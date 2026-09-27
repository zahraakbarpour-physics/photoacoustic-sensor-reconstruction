60-Day Roadmap: Reconstructing Missing Sensor Data in Photoacoustic Arrays
Project Objective: To simulate, implement, and evaluate signal processing techniques (Linear and Spline Interpolation) for reconstructing missing or inactive sensor data in a photoacoustic array and to assess the impact of this reconstruction on the final image quality using SNR, PSNR, and SSIM metrics.

Note: This schedule is designed for ~1 hour of daily focused work (coding + study).

Phase 1: Infrastructure, Version Control, and Python Fundamentals (Days 1-7)
Goal: Set up a professional development environment and master the essential Python libraries for array manipulation.

[ ] Day 1: Initialize the GitHub repository. Create the project structure: data/ (for raw/processed datasets), src/ (source code), notebooks/ (Jupyter notebooks for experimentation), and an initial README.md.

[ ] Day 2: Practice Git workflow (git add, commit, push) and integrate Git with VS Code for seamless daily commits.

[ ] Day 3-4: Review NumPy fundamentals. Focus on N-dimensional arrays, slicing, and matrix operations (essential for handling sensor matrices).

[ ] Day 5-6: Review Matplotlib and SciPy. Practice plotting 1D time-series signals and visualizing 2D matrices as images (plt.imshow).

[ ] Day 7: Create a requirements.txt file listing all dependencies. Make the first structural commit to GitHub.

Phase 2: Photoacoustic Physics & Numerical Simulation (Days 8-20)
Goal: Understand the forward problem and simulate the initial photoacoustic data.

[ ] Day 8-10: Study the physics of the photoacoustic effect (optical absorption, thermal expansion, and the generation of acoustic waves).

[ ] Day 11-13: Explore simulation tools. Learn to use the k-Wave toolbox (via MATLAB or its Python wrappers/alternatives like j-Wave) to simulate acoustic wave propagation in biological tissues.

[ ] Day 14-16: Define a simple 2D computational environment (phantom) containing point sources or simulated blood vessels.

[ ] Day 17-18: Define the acoustic sensor array (e.g., a 128-element linear array or a semi-circular array) within the simulation grid.

[ ] Day 19-20: Run the simulation to extract the time-series pressure data from all sensors. Save the output as .npy or .mat files in the data/ folder and commit.

Phase 3: Base Image Reconstruction Algorithm (Days 21-28)
Goal: Solve the inverse problem to create a baseline image from complete sensor data.

[ ] Day 21-23: Study the underlying math of the Delay-and-Sum (DAS) beamforming algorithm. Understand the Time-of-Flight (ToF) calculations.

[ ] Day 24-26: Implement the DAS algorithm from scratch in Python to map the 2D sensor data matrix into a reconstructed 2D image.

[ ] Day 27-28: Test the DAS algorithm on the simulated data to generate the "Ground Truth" image (using 100% of the sensors). Push the code to GitHub.

Phase 4: Sensor Degradation Simulation & Interpolation Methods (Days 29-40)
Goal: Simulate hardware failure and implement signal processing techniques for data recovery.

[ ] Day 29-30: Create a masking function to simulate defective sensors. Implement both random dropout (e.g., 30% random loss) and block dropout (contiguous missing sensors).

[ ] Day 31-32: Run the DAS algorithm on the incomplete data to visualize the degraded image artifacts. Save these images for baseline comparison.

[ ] Day 33-35: Study and implement Linear Interpolation (using scipy.interpolate.interp1d) on the raw sensor space to estimate the missing time-series signals.

[ ] Day 36-38: Study and implement Spline Interpolation to generate smoother, non-linear approximations of the missing signals.

[ ] Day 39-40: Re-run the DAS reconstruction using the imputed data (once for Linear, once for Spline). Commit the interpolation scripts.

Phase 5: Quantitative Image Quality Evaluation (Days 41-50)
Goal: Objectively measure the performance of the reconstruction methods.

[ ] Day 41-43: Study Signal-to-Noise Ratio (SNR). Implement a custom Python function to calculate the SNR of the reconstructed images.

[ ] Day 44-46: Study Peak Signal-to-Noise Ratio (PSNR). Import skimage.metrics and compute the PSNR of the repaired images against the Ground Truth.

[ ] Day 47-49: Study the Structural Similarity Index Measure (SSIM) to evaluate perceptual quality. Calculate SSIM using skimage.metrics.structural_similarity.

[ ] Day 50: Automate the extraction of these metrics for different dropout percentages and save the results to a CSV/Excel file.

Phase 6: Data Analysis, Refactoring, and GitHub Polish (Days 51-60)
Goal: Finalize the project for public viewing and academic portfolio presentation.

[ ] Day 51-53: Visualize the results using Matplotlib. Create bar charts and line graphs comparing SNR, PSNR, and SSIM across the different interpolation methods and dropout rates.

[ ] Day 54-55: Refactor code. Move logic from Jupyter Notebooks into clean, modular Python scripts (e.g., simulate.py, reconstruct.py, metrics.py).

[ ] Day 56-58: Write the comprehensive final README.md. Include sections: Abstract, Prerequisites, How to Run, and Results (featuring visual side-by-side comparisons of the reconstructed images).

[ ] Day 59: Final code review. Clean up comments, remove debugging print statements, and ensure the code runs flawlessly on a fresh machine.

[ ] Day 60: Make the GitHub repository public. Add the repository link to your CV/Resume.
