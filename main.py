import matplotlib.pyplot as plt
import numpy as np
from sys import argv


def will_it_float(string: str) -> float:
    try:
        float(string)
        return True
    except ValueError:
        return False


def acceleration(position: float, frequency: float) -> float:
    return -pow(frequency, 2) * position


if __name__ == "__main__":
    if len(argv) != 5 or not will_it_float(argv[1]) or\
            not will_it_float(argv[2]) or not will_it_float(argv[3])\
            or not will_it_float(argv[4]):
        print(("Usage: python main.py <initial-position> <initial-velocity> "
              "<time> <frequency>"))
        exit(-1)

    initial_position = float(argv[1])
    initial_velocity = float(argv[2])
    end_time = float(argv[3])
    frequency = float(argv[4])

    time_samples, step_size = np.linspace(0, end_time, num=1000, retstep=True)
    position_samples = np.zeros_like(time_samples)
    position_samples[0] = initial_position
    velocity = initial_velocity

    for i in range(1, len(time_samples)):
        position_samples[i] = position_samples[i-1] + step_size * velocity
        velocity += step_size * acceleration(position_samples[i], frequency)

    plt.plot(time_samples, position_samples)
    plt.show()
