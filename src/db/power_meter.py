from dataclasses import dataclass

import pandas as pd


@dataclass(init=True)
class PowerMeterContext:
    def __init__(self, sample_per_second: int, file_path: str):
        self.sample_per_second: int = sample_per_second
        self.file_path: str = file_path
        self.fs = open(file_path, 'r')


def sample_energy_watts(c: PowerMeterContext, t_sec: int) -> float:
    df = pd.read_csv(c.fs, on_bad_lines='skip')
    t = t_sec * c.sample_per_second
    energy_watts_samples = df.tail(t)[:, -1]
    return energy_watts_samples.sum()
