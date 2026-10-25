
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from simulate import simulate_sensor_signals
from reconstruct import delay_and_sum


def run_pipeline():
    # Project output directory
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Simulate sensor signals
    sensor_x, time, signals = simulate_sensor_signals()
    sensor_y = np.zeros_like(sensor_x)

    # Step 2: Define reconstruction grid
    x_values = np.linspace(-15e-3, 15e-3, 100)
    y_values = np.linspace(0, 30e-3, 100)
    X, Y = np.meshgrid(x_values, y_values)

    # Step 3: Reconstruct image
    image = delay_and_sum(
        signals, time, sensor_x, sensor_y, X, Y, 1500
    )

    # Step 4: Estimate source location
    max_index = np.unravel_index(np.argmax(image), image.shape)
    estimated_x = float(X[max_index])
    estimated_y = float(Y[max_index])

    # Step 5: Save reconstruction image
    image_path = output_dir / "day58_das_reconstruction.png"

    plt.figure(figsize=(8, 6))
    plt.imshow(
        image,
        extent=[
            x_values[0] * 1000,
            x_values[-1] * 1000,
            y_values[-1] * 1000,
            y_values[0] * 1000,
        ],
        aspect="auto",
        cmap="hot",
    )
    plt.colorbar(label="Summed signal intensity")
    plt.scatter(
        [5.0], [20.0],
        marker="x", color="cyan", label="True source"
    )
    plt.scatter(
        [estimated_x * 1000],
        [estimated_y * 1000],
        marker="o", facecolors="none",
        edgecolors="lime", label="Estimated source"
    )
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.title("DAS Reconstruction")
    plt.legend()
    plt.tight_layout()
    plt.savefig(image_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    # Step 6: Save numerical results
    results = {
        "day": 58,
        "method": "Delay-and-Sum (DAS)",
        "number_of_sensors": int(len(sensor_x)),
        "signal_matrix_shape": list(signals.shape),
        "image_shape": list(image.shape),
        "maximum_intensity": float(np.max(image)),
        "estimated_source_x_mm": estimated_x * 1000,
        "estimated_source_y_mm": estimated_y * 1000,
        "true_source_x_mm": 5.0,
        "true_source_y_mm": 20.0,
        "image_file": image_path.name,
    }

    results_path = output_dir / "day58_das_results.json"
    with open(results_path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print("Pipeline completed successfully.")
    print("Image saved to:", image_path)
    print("Results saved to:", results_path)
    print(json.dumps(results, indent=4))

    return image, results


if __name__ == "__main__":
    run_pipeline()
