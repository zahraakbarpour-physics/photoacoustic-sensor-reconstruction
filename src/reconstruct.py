
import numpy as np


def delay_and_sum(
    signals,
    time,
    sensor_x,
    sensor_y,
    X,
    Y,
    c
):
    """
    Reconstruct a 2D image using Delay-and-Sum (DAS).

    Parameters
    ----------
    signals : array
        Signal matrix with shape (num_sensors, num_time_samples).
    time : array
        Time axis in seconds.
    sensor_x, sensor_y : array
        Sensor coordinates in meters.
    X, Y : array
        Image grid coordinates in meters.
    c : float
        Speed of sound in meters per second.

    Returns
    -------
    image : array
        Reconstructed 2D image.
    """

    num_sensors = signals.shape[0]

    image = np.zeros(X.shape, dtype=float)

    for i in range(num_sensors):

        # Distance from every image pixel to sensor i
        distance = np.sqrt(
            (X - sensor_x[i])**2
            + (Y - sensor_y[i])**2
        )

        # Predicted travel time
        tof = distance / c

        # Convert time to sample indices
        sample_indices = np.rint(
            (tof - time[0]) / (time[1] - time[0])
        ).astype(int)

        # Only use indices inside the recorded signal
        valid = (
            (sample_indices >= 0)
            & (sample_indices < len(time))
        )

        sensor_contribution = np.zeros(X.shape)

        sensor_contribution[valid] = signals[
            i, sample_indices[valid]
        ]

        # Add this sensor's contribution
        image += sensor_contribution

    return image
