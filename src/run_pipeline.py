
import numpy as np

from simulate import simulate_sensor_signals
from reconstruct import delay_and_sum


def run_pipeline():
    # Step 1: Simulate sensor signals
    sensor_x, time, signals = simulate_sensor_signals()
    sensor_y = np.zeros_like(sensor_x)

    # Step 2: Define reconstruction grid
    x_values = np.linspace(-15e-3, 15e-3, 100)
    y_values = np.linspace(0, 30e-3, 100)
    X, Y = np.meshgrid(x_values, y_values)

    # Step 3: Reconstruct the image using DAS
    image = delay_and_sum(
        signals,
        time,
        sensor_x,
        sensor_y,
        X,
        Y,
        1500,
    )

    # Step 4: Report results
    max_index = np.unravel_index(
        np.argmax(image), image.shape
    )
    estimated_x = X[max_index]
    estimated_y = Y[max_index]

    print("Pipeline completed successfully.")
    print("Number of sensors:", len(sensor_x))
    print("Signal matrix shape:", signals.shape)
    print("Reconstructed image shape:", image.shape)
    print("Maximum intensity:", np.max(image))
    print(
        "Estimated source location: "
        f"({estimated_x * 1000:.2f}, "
        f"{estimated_y * 1000:.2f}) mm"
    )

    return image


if __name__ == "__main__":
    run_pipeline()
