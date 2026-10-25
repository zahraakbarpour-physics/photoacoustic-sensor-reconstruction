
import numpy as np


def simulate_sensor_signals(
    num_sensors=32,
    num_samples=600,
    sampling_frequency=10e6,
    sound_speed=1500,
    source_x=5e-3,
    source_y=20e-3,
    pulse_width=1.5e-6,
):
    """
    Generate synthetic photoacoustic signals for a linear sensor array.

    Returns
    -------
    sensor_positions : ndarray
        Sensor x-positions in meters.
    time : ndarray
        Sampling times in seconds.
    signals : ndarray
        Signal matrix with shape (num_sensors, num_samples).
    """
    dt = 1 / sampling_frequency
    time = np.arange(num_samples) * dt

    sensor_positions = np.linspace(-15e-3, 15e-3, num_sensors)
    signals = np.zeros((num_sensors, num_samples))

    for i, sensor_x in enumerate(sensor_positions):
        distance = np.sqrt(
            (sensor_x - source_x) ** 2 + source_y ** 2
        )
        arrival_time = distance / sound_speed

        signals[i] = np.exp(
            -0.5 * ((time - arrival_time) / pulse_width) ** 2
        )

    return sensor_positions, time, signals


if __name__ == "__main__":
    positions, time, signals = simulate_sensor_signals()

    print("Simulation completed successfully.")
    print("Number of sensors:", len(positions))
    print("Signal matrix shape:", signals.shape)
    print("Sampling frequency: 10 MHz")
