
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
from src.simulate import simulate_sensor_signals
from src.reconstruct import delay_and_sum


def test_das_reconstruction():
    sensor_x, time, signals = simulate_sensor_signals()
    sensor_y = np.zeros_like(sensor_x)

    x_values = np.linspace(-15e-3, 15e-3, 100)
    y_values = np.linspace(0, 30e-3, 100)
    X, Y = np.meshgrid(x_values, y_values)

    image = delay_and_sum(
        signals, time, sensor_x, sensor_y, X, Y, 1500
    )

    assert image.shape == X.shape
    assert np.all(np.isfinite(image))
    assert np.max(image) > 0

    print("DAS reconstruction test passed!")
    print("Image shape:", image.shape)
    print("Maximum intensity:", np.max(image))

    # Find the location of maximum image intensity
    max_index = np.unravel_index(np.argmax(image), image.shape)
    estimated_x = X[max_index]
    estimated_y = Y[max_index]

    print(
        f"Estimated source location: "
        f"({estimated_x * 1000:.2f}, {estimated_y * 1000:.2f}) mm"
    )
    print("True source location: (5.00, 20.00) mm")


if __name__ == "__main__":
    test_das_reconstruction()
