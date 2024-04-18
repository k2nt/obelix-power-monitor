from dataclasses import dataclass

from io import TextIOWrapper
from pathlib import Path


@dataclass(init=True)
class PowerMeter:
    fs: TextIOWrapper


def new(path: Path | str) -> PowerMeter:
    return PowerMeter(open(path, 'r'))


def sample_energy_watts(m: PowerMeter, t_seconds: int) -> float:
    ...
